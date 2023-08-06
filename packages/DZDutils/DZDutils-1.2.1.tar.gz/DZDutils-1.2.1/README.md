# DZDuitls

Python tool collection

## About

**Maintainer**: tim.bleimehl@dzd-ev.de

**Licence**: MIT

**Purpose**: Collection of homemade Python tools of the German Center for Diabetes Research

[[_TOC_]]


## Install

`pip3 install DZDutils`

or if you need the current dev version:

`pip3 install git+https://git.connect.dzd-ev.de/dzdpythonmodules/dzdutils.git`


## Modules

### DZDutils.inspect

**object2html**

Opens the webbrowser and let you inspect any object / dict with jquery jsonviewer

```python
from DZDutils.inspect import object2html
my_ultra_complex_dict = {"key":"val"}
object2html(my_ultra_complex_dict)
``` 

### DZDutils.list

#### chunks

Breaks up a list in shorter lists of given length

```python
from DZDutils.list import chunks
my_ultra_long_list = [1,2,3,4,5,6,7,8,9,10]
for chunk in chunks(my_ultra_long_list, 3)
    print(chunk)
```

Output:

```python
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
[10]
``` 


#### divide

Breaks up a list in a given amount of shorter lists

```python
from DZDutils.list import divide
my_ultra_long_list = [1,2,3,4,5,6,7,8,9,10]
for chunk in divide(my_ultra_long_list, 3)
    print(chunk)
```

Output:

```python
[1, 2, 3, 4]
[5, 6, 7]
[8, 9, 10]
``` 

### DZDutils.neo4j


#### wait_for_db_boot

Wait for a neo4j to boot up. If timeout is expired it will raise the last error of the connection expception for debuging.
The argument `neo4j` must be a dict of py2neo.Graph() arguments -> https://py2neo.org/2021.1/profiles.html#individual-settings

```
from DZDutils.neo4j import wait_for_db_boot
wait_for_db_boot(neo4j={"host": "localhost"}, timeout_sec=120)
```


#### nodes_to_buckets_distributor

Divide a bunch of nodes into multiple buckets (labels with a prefix and sequential numbering e.b. "BucketLabel1, BucketLabel2, ...")

Supply a query return nodes. Get a list of str containg the buckets label names


```python
import py2neo
from DZDutils.neo4j import nodes_to_buckets_distributor

g = py2neo.Graph()

# Create some testnodes

g.run(f"UNWIND range(1,10) as i CREATE (:MyNodeLabel)")

labels = nodes_to_buckets_distributor(
            g,
            query=f"MATCH (n:MyNodeLabel) return n",
            bucket_count=3,
            bucket_label_prefix="Bucket",
        )

print(labels)
```
Output:

`['Bucket0','Bucket1','Bucket2']`

Each of our `:MyNodeLabel`-Nodes has now applied one of the bucket labels


#### run_periodic_iterate

Abstraction function for [`apoc.periodic.iterate`](https://neo4j.com/labs/apoc/4.1/overview/apoc.periodic/apoc.periodic.iterate/) with proper error handling and less of the string fumbling

```python
import py2neo
from DZDutils.neo4j import run_periodic_iterate

g = py2neo.Graph()

# Create some node per iterate
run_periodic_iterate(
        g,
        cypherIterate="UNWIND range(1,100) as i return i",
        cypherAction="CREATE (n:_TestNode) SET n.index = i",
        parallel=True,
    )

# set some props per iterate
run_periodic_iterate(
        g,
        cypherIterate="MATCH (n:_TestNode) return n",
        cypherAction="SET n.prop = 'MyVal'",
        parallel=True,
    )
```

##### Error Handling

When using `apoc.periodic.iterate` manual you have to parse the result table for errors and interpret the result if and how a query failed.


With `run_periodic_iterate` you dont have to anymore.

Lets have an example and write some faulty query

```python
import py2neo
from DZDutils.neo4j import run_periodic_iterate

g = py2neo.Graph()

# Create some node per iterate
run_periodic_iterate(
        g,
        cypherIterate="UNWIND range(1,100) as i return i",
        cypherAction="f*** ohnooo i cant write proper cypher",
        parallel=True,
    )
```

This will result in an exception: 

```
DZDutils.neo4j.Neo4jPeriodicIterateError: Error on 100 of 100 operations. ErrorMessages:

 Invalid input 'f': expected
  ","
  "CALL"
  "CREATE"
[...]
  "WITH"
  <EOF> (line 1, column 46 (offset: 45))
"UNWIND $_batch AS _batch WITH _batch.i AS i  f*** ohnooo i cant write proper cypher"
```

As wee see we get immediately feedback if and how the query failed

