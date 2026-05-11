import ray
import time

# Initialize Ray (runs locally or connects to a cluster)
ray.init()

@ray.remote
def process_data(x):
    time.sleep(1)  # Simulate a heavy task
    return x * x

# Launch 4 tasks in parallel
futures = [process_data.remote(i) for i in range(4)]

# Retrieve the results when they are ready
results = ray.get(futures)
print(results)  # [0, 1, 4, 9]
