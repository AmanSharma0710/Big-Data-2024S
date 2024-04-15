import sys
import re
from operator import add

from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark-submit assignment-3-20CS30063.py <datafile_name>")
        sys.exit(1)

    spark = SparkSession.builder.appName("TriangleCount").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    num_edges = lines.count()
    node_degree = lines.flatMap(lambda x: re.split('\W+', x)) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    # Get the number of nodes with edges > sqrt(num_edges)
    hhnodes = node_degree.filter(lambda x: x[1] > num_edges ** 0.5).map(lambda x: x[0])
    print("No of heavy hitter nodes:", hhnodes.count())
    edges = lines.map(lambda x: re.split('\W+', x))
    adj_list = lines.map(lambda x: re.split('\W+', x)) \
                .flatMap(lambda x: [(x[0], x[1]), (x[1], x[0])]) \
                .groupByKey().mapValues(list).collectAsMap()
    hhtriangles = hhnodes.cartesian(hhnodes).filter(lambda x: x[0] < x[1]) \
                    .cartesian(hhnodes).filter(lambda x: x[0][1] < x[1]) \
                    .map(lambda x: (x[0][0], x[0][1], x[1]))
    # Count the number of valid triangles in hhtriangles
    numhhtriangles = hhtriangles.filter(lambda x: x[0] in adj_list and x[1] in adj_list and x[2] in adj_list) \
                    .filter(lambda x: x[1] in adj_list[x[0]] and x[2] in adj_list[x[0]] and x[2] in adj_list[x[1]]) \
                    .count()
    # Filter out the edges with both nodes as heavy hitters
    hashmap_hhnodes = set(hhnodes.collect())
    non_hh_edges = edges.filter(lambda x: x[0] not in hashmap_hhnodes or x[1] not in hashmap_hhnodes)
    def get_common_neighbors(x):
        triangle_list = []
        list1 = adj_list[x[0]]
        list2 = adj_list[x[1]]
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        for neighbor in list1:
            if neighbor in list2:
                tr = [x[0], x[1], neighbor]
                tr.sort()
                triangle_list.append(tuple(tr))
        # We return a list of triangles instead of number so count of triangles that have one heavy hitter edge is correct and no double counting errors occur
        return triangle_list
        
    nonhhtriangles = non_hh_edges.flatMap(get_common_neighbors)
    if nonhhtriangles.isEmpty():
        numnonhhtriangles = 0
    else:
        numnonhhtriangles = nonhhtriangles.distinct().count()
    print("No of triangles:", int(numhhtriangles + numnonhhtriangles))
    spark.stop()