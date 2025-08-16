# Multiprocessing refers to the concurrent execution of multiple processes to achieve parallelism and utilize multiple CPU cores effectively. Unlike threading which operates within a single process and shares memory space, multiprocessing involves separate processes with their own memory space, providing a higher degree of isolation and avoiding the Global Interpreter Lock limitation.
# Example
# The multiprocessing module provides a similar interface to the threading module but for creating processes instead of threads. To create a new process, you can use the `multiprocessing.Process` class. You can pass a function as the target argument to the process constructor, and it will be executed when the process starts. You can also pass any arguments required by the target function as keyword arguments.
import multiprocessing


def print_message(message):
    print(message)
    return


# Create a new process
process = multiprocessing.Process(target=print_message, args=("Hello, World!",))

# Start the process
process.start()

# Wait for the process to finish execution
process.join()

print("Process finished execution.")

# Process communication:
# - Multiprocessing allows processes to communicate with each other using shared memory, pipes, or queues. You can use the `multiprocessing.Queue` class to create a queue for communication between processes. Processes can put data into the queue using the `put` method and retrieve data using the `get` method.
# Example using a queue:
import multiprocessing


def worker(queue):
    message = queue.get()
    print(f"Worker received message: {message}")
    queue.put(f"Worker processed message: {message}")
    return


# Create a queue
queue = multiprocessing.Queue()

# Create a process to send a message
send_process = multiprocessing.Process(target=worker, args=(queue,))

# Create a process to receive and process the message
receive_process = multiprocessing.Process(target=worker, args=(queue,))

# Start the processes
send_process.start()
receive_process.start()

# Send a message to the queue
queue.put("Hello, World!")

# Wait for the processes to finish execution
send_process.join()
receive_process.join()

print("Processes finished execution.")

# Pool of process:
# - The `multiprocessing.Pool` class provides a pool of worker processes for executing tasks. You can use the `Pool.apply_async` method to submit tasks to the pool and retrieve the results asynchronously. The `Pool.close` method should be called before the pool is destroyed to prevent any new tasks from being submitted.
# Example using a pool of processes:
import multiprocessing


def worker(message):
    print(f"Worker received message: {message}")
    return


# Create a pool of worker processes
pool = multiprocessing.Pool(processes=4)

# Submit tasks to the pool
results = []
for i in range(10):
    result = pool.apply_async(worker, args=(f"Message {i}",))
    results.append(result)

# Wait for all tasks to finish execution
for result in results:
    result.get()

pool.close()
pool.join()

print("Pool of processes finished execution.")

# Global Interpreter Lock (GIL) avoidance:
# - The Global Interpreter Lock (GIL) is a mechanism in Python that prevents multiple threads from executing native code at the same time. This lock is necessary to ensure that only one thread can execute Python bytecodes at a time, which is necessary for maintaining thread safety. Multiprocessing can help overcome this limitation by creating separate processes, each with its own memory space, allowing for parallel execution. However, the GIL can still cause performance issues in certain scenarios, such as CPU-bound tasks or I/O-bound tasks, where multiple threads can compete for resources.
# Muliprocessing can be used to achieve parallelism and utilize multiple CPU cores effectively, but it is important to note that the GIL does not affect the performance of CPU-bound tasks or I/O- bound tasks.
# Be cautious when sharing mutable data between processes, as modifying shared data can lead to race conditions and inconsistent behavior. Instead, use thread-safe data structures and use thread-safe communication mechanisms such as queues or shared memory.
# Prefer the concurrent.futures.ProcessPoolExecutor for creating and managing processes, as it provides a higher-level interface for managing processes and tasks. It automatically handles the GIL and provides more efficient parallel execution.
# Be mind-full of the overhead of creating and managing processes, as they can introduce additional complexity and resource usage. Consider using threading or multiprocessing as appropriate based on the specific requirements and performance requirements of your application.
