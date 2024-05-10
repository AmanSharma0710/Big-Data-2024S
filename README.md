# Big Data Processing

## Assignment 1

First assignment involves writing a multi-threaded priority queue in Python. Using this queue we solve the top-k similarity problem, where given some vectors and a query vector, we need to find the top-k vectors closest to the query vector, considering cosine similarity.

```
python3 <code.py> <data file> <query vector file> <# of threads> <value of k>
```
where data file contains the ID's of the vectors and the vectors in a space seperated manner, one in each line. The query vector file contains just the query vector.

## Assignment 2

This assignment involved writing the map function of a map-reduce operation, including using a limited sized buffer in memory to store the intermediate output and sorting files on disk if necessary. The map function takes the text file and produces the most frequent k key bi-grams (one bi-gram in one line) based on their count in the input file. A key  bi-gram  is  an  ordered  sequence  of  two  words  where  the  second  word  appears  immediately  after  the first word in the input text file.

It stores these bigrams in a dictionary in memory, but when the memory buffer fills up, it is flushed to storage and then all the bigrams are merged and sorted on disk and top k ones printed.

```
python3 <code.py> <input file> <buffer size (in MB)> <value of k>
```

## Assignment 3

The final assignment involved writing a spark program that counts the number of triangles in an undirected unweighted graph. We first find the heavy hitter nodes, which are nodes with degree greater or equal to square root of the number of edges in the graph. Then the triangles can be of two types:
 - All three nodes in the triangle are heavy hitter, we can count there by considering all tuples of heavy hitter nodes and checking which are valid triangles
 - We consider all edges that have at least one non-heavy hitter node and then all the common neighbours of the nodes that have this edge form a triangle with the two nodes of the edge, and we count these taking care of repetitions
 ```
spark-submit <code.py> <input file>
```