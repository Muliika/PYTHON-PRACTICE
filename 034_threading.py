# Threading in python refers to the concurrent execution of of multiple threads within the same thread. Threads are light weight execution units that spare the same memory space allowing them to communicate and interact directly with each other. Threading is a way to achieve concurrency, where multiple tasks are executed simultaneously, improving performance and responsiveness in certain types of apps.
# Thread creation:
# - To create a new thread in Python, you can use the `threading.Thread` class. You can pass a function as the target argument to the thread constructor, and it will be executed when the thread starts. You can also pass any arguments required by the target function as keyword arguments.

# Example:
import threading
import time


def print_message(message):
    print(message)


thread = threading.Thread(target=print_message, args=("Hello, World!",))

# Starting the thread
thread.start()

# Joining the thread
thread.join()

print("Thread finished execution.")

# Thread synchronization:
# - Thread synchronization is a mechanism to ensure that multiple threads access and modify shared resources in a safe and controlled manner. Python provides various synchronization primitives such as locks, semaphores, and condition variables to handle thread synchronization.

# Example:
import threading

# Lock
counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    with lock:
        counter += 1


# Creating threads
threads = [threading.Thread(target=increment_counter)]
for tread in threads:
    thread.start()
for tread in threads:
    thread.join()

print("Counter: ", counter)


import queue

# Thread communication:
# - Thread communication is a mechanism to exchange information between threads. Python provides various communication mechanisms such as shared memory, queues, and event objects to handle thread communication.
# Example:
import threading

# Queue


def producer(queue):
    for i in range(5):
        queue.put(i)


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print("Consumed: ", item)
        queue.task_done()


q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
q.put(None)
consumer_thread.join()

print("Finished.")


# Global interpreter lock
# - The Global Interpreter Lock (GIL) is a mechanism in Python that prevents multiple threads from executing native code at the same time. This lock is necessary to ensure that only one thread can execute Python bytecodes at a time, which is necessary for maintaining thread safety. GIL can cause performance issues in certain scenarios, such as CPU-bound tasks or I/O-bound tasks, where multiple threads can compete for resources.
# However threading can still be useful for I/O-bound tasks, as it allows multiple threads to execute concurrently. such as network I/O, database I/O, and file I/O operations can benefit from multiple threads.

# considerations and best practices:
# - Threading should be used judiciously and only when necessary. Over-using threads can lead to increased memory usage and decreased performance. It is recommended to use threading only when necessary and when the benefits of concurrency outweigh the drawbacks.
# - Use thread synchronization mechanisms, such as locks, semaphores, or condition variables, to ensure thread safety and prevent race conditions.
# - Avoid using global variables or shared resources in threads, as they can lead to data races and inconsistent behavior. Instead, use thread-safe data structures and communication mechanisms such as queues or shared memory.
# -Use threading for I/O-bound tasks, as it allows multiple threads to execute concurrently, improving performance and reducing latency.
# -Be cautious when sharing mutable data between threads, as modifying shared data can lead to race conditions and inconsistent behavior. Instead, use immutable data structures and use thread-safe data structures, such as locks, semaphores, or condition variables, to ensure thread safety.
# -Prefer higher-level concurrency libraries and frameworks, such as asyncio, concurrent.futures, or multiprocessing, over low-level threading and multiprocessing for better performance and scalability.
# prefer higher level threading constructs provided by the concurent.features module over low-level threading and multiprocessing constructs.
