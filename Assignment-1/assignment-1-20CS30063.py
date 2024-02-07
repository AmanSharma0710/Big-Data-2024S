import threading
import sys
import heapq
from numpy import dot
from numpy.linalg import norm

def find_top_k(data, query, k, start, end, thread_id):
    # Push the ID and the distance of the points into a heap
    heap = []
    for i in range(start, end):
        cosine_similarity = dot(data[i][1], query) / (norm(data[i][1]) * norm(query))
        heapq.heappush(heap, (-cosine_similarity, data[i][0]))
    
    # Pop the top k elements from the heap
    top_k = []
    for i in range(k):
        if len(heap) == 0:
            break
        top_k.append(heapq.heappop(heap))
    global thread_outputs
    thread_outputs[thread_id] = top_k


if __name__ == "__main__":
    # Get the command line arguments
    if len(sys.argv) != 5:
        print("Usage: python assignment-1-20CS30063.py <data file> <query item file> <# threads> <value of k>")
        sys.exit(1)
    data_file = sys.argv[1]
    query_file = sys.argv[2]
    num_threads = int(sys.argv[3])
    k = int(sys.argv[4])

    # Read the data file
    data = []
    with open(data_file, "r") as f:
        for line in f:
            line_data = line.strip().split()
            data.append([int(line_data[0]), [float(x) for x in line_data[1:]]])
    
    # Read the query file
    query = []
    with open(query_file, "r") as f:
        for line in f:
            query.append([float(x) for x in line.strip().split()])
    
    # Create a list to store outputs of threads
    thread_outputs = [None for i in range(num_threads)]

    # Create threads
    threads = []
    for i in range(num_threads):
        start = i * len(data) // num_threads
        end = (i + 1) * len(data) // num_threads
        thread = threading.Thread(target=find_top_k, args=(data, query[0], k, start, end, i))
        threads.append(thread)
    
    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for the threads to finish
    for thread in threads:
        thread.join()

    # Merge the outputs of the threads
    top_k = []
    for i in range(num_threads):
        for item in thread_outputs[i]:
            heapq.heappush(top_k, item)
    
    # Print the top k elements
    for i in range(k):
        if len(top_k) == 0:
            break
        item = heapq.heappop(top_k)
        print(item[1], -item[0])