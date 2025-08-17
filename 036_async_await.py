# Asynchronous programming allows you to write concurrent code that executes in a non-blocking manner that can efficiently handle I/O-bound tasks, such as network I/O, database I/O, and file I/O operations.

# asnyc await keywords
# - Asynchronous programming is supported by Python 3.5 and later versions. The `async` and `await` keywords are used to define asynchronous functions and await for the completion of asynchronous operations.

# Async is used to mark a function as asynchronous, and await is used to pause the execution of the current function and wait for the completion of another asynchronous function.
# An asynchronous function can have multiple `await` expressions, which allows it to be used in a multi-threaded or multi-process environment.

# Asynchronous functions:
# Example of asynchronous function
import asyncio


async def print_message(message):
    print(message)
    await asyncio.sleep(1)  # Simulate I/O-bound operation
    print("Message printed")
    return


# Event loop
loop = asyncio.get_event_loop()

# Run the asynchronous function
loop.run_until_complete(print_message("Hello, World!"))


# Async with await expressions:
# Example of asynchronous function with await expressions
async def print_messages(messages):
    for message in messages:
        await print_message(message)
        await asyncio.sleep(1)  # Simulate I/O-bound operation
        print("Messages printed")
        return
    # Close the event loop
    loop.close()
    return


# Run the asynchronous function with await expressions
loop.run_until_complete(print_messages(["Message 1", "Message 2", "Message 3"]))


# Asynchronous with coroutines:
# Example of asynchronous function with coroutines
async def print_messages_coroutine(messages):
    for message in messages:
        await print_message(message)
        await asyncio.sleep(1)  # Simulate I/O-bound operation
        print("Messages printed")
        return
    # Close the event loop
    loop.close()
    return


# Run the asynchronous function with coroutines
loop.run_until_complete(
    print_messages_coroutine(["Message 1", "Message 2", "Message 3"])
)

# The even loop schedules and executes asynchronous functions, handles awaitable objects and manages concurrency.
# You typically interact with the event loop using functions like asyncio.run(), asyncio.create_task() and asyncio.gather().


# Example:
async def main():
    task1 = asyncio.create_task(print_message("Task 1"))
    task2 = asyncio.create_task(print_message("Task 2"))
    await asyncio.gather(task1, task2)


asyncio.run(main())

# Concurrency and parallelism:
# Asynchronous programming enables concurrent execution of multiple tasks. Tasks can be executed in parallel, resulting in improved performance and efficiency. asyncio uses a single event loop to manage multiple concurrent tasks.
# To achieve parallelism, you can combine asynchronous programming with multiprocessing (asyncio.run_in_executor())


# Benefits of asynchronous programming:
# - Improved performance: Asynchronous programming can execute multiple tasks concurrently, reducing the time taken to complete the entire program. This can lead to faster response times and improved user experience.
# - Efficient resource utilization: Asynchronous programming can utilize multiple CPU cores or threads, improving the performance of CPU-bound tasks.
# - Scalability: Asynchronous programming can handle a large number of concurrent tasks, improving the scalability of the program.
# - Better error handling: Asynchronous programming allows you to handle exceptions and errors in a more graceful manner, avoiding crashes and providing meaningful error messages.
