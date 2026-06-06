#Multi-threading in Python:
#When to use multi-threading:
#1. I/O-bound tasks: If your program spends a lot of time waiting for input/output operations (like reading/writing files, network requests), multi-threading can help improve performance by allowing other threads to run while one thread is waiting.
#2. GUI applications: In graphical user interfaces, multi-threading can keep the interface responsive while performing background tasks.
#3. Concurrent tasks: If you have multiple tasks that can run concurrently (like downloading multiple files), multi-threading can help manage these tasks efficiently.
#Example of multi-threading in Python using the threading module:
import threading
import time
def print_numbers():
    for i in range(5):
        print(f"Numbers:{i}")
        time.sleep(2)  # Simulate a time-consuming task
def print_letters():
    for letter in 'ABCDE':
        print(f"Letters:{letter}")
        time.sleep(2)  # Simulate a time-consuming task
# Create threads for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
t = time.time()
thread1.start()
thread2.start() # Start both threads
thread1.join() # Wait for thread1 to finish
thread2.join() # Wait for thread2 to finish

finished_time = time.time() -  t
print(f"Time taken with threading: {finished_time} seconds")
