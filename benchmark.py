import time
import redis
import hazelcast

def benchmark_redis():
    redis_host = 'localhost'
    redis_port = 6379
    r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
    
    # Write benchmark
    start_time = time.time()
    for i in range(100000):
        r.set(f"key{i}", f"value{i}")
    end_time = time.time()
    write_time = end_time - start_time
    print(f"Redis write time for 100,000 entries: {write_time:.4f} seconds")

    # Read benchmark
    start_time = time.time()
    for i in range(100000):
        r.get(f"key{i}")
    end_time = time.time()
    read_time = end_time - start_time
    avg_read_time = read_time / 100000
    print(f"Redis average read time: {avg_read_time:.8f} seconds")
    
    # Cleanup
    start_time = time.time()
    for i in range(100000):
        r.delete(f"key{i}")
    end_time = time.time()
    cleanup_time = end_time - start_time
    print(f"Redis cleanup time for 100,000 entries: {cleanup_time:.4f} seconds")


def benchmark_hazelcast():
    cluster_name = "hello-world"
    client = hazelcast.HazelcastClient(cluster_name=cluster_name)
    my_map = client.get_map("my-distributed-map").blocking()

    # Write benchmark
    start_time = time.time()
    for i in range(100000):
        my_map.put(f"key{i}", f"value{i}")
    end_time = time.time()
    write_time = end_time - start_time
    print(f"Hazelcast write time for 100,000 entries: {write_time:.4f} seconds")

    # Read benchmark
    start_time = time.time()
    for i in range(100000):
        my_map.get(f"key{i}")
    end_time = time.time()
    read_time = end_time - start_time
    avg_read_time = read_time / 100000
    print(f"Hazelcast average read time: {avg_read_time:.8f} seconds")

    # Cleanup
    start_time = time.time()
    for i in range(100000):
        my_map.remove(f"key{i}")
    end_time = time.time()
    cleanup_time = end_time - start_time
    print(f"Hazelcast cleanup time for 100,000 entries: {cleanup_time:.4f} seconds")

    client.shutdown()


if __name__ == "__main__":
    print("Starting Redis benchmark...")
    benchmark_redis()

    print("\nStarting Hazelcast benchmark...")
    benchmark_hazelcast()
