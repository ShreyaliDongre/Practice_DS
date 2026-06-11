#Multiprocessing allows you to run multiple processes in parallel, 
# which can be useful for CPU-bound tasks.
# CPU-bound tasks: If your program spends a lot of time performing computations,
# multiprocessing can help improve performance by utilizing multiple CPU cores. 
# Here's an example of how to use the multiprocessing module in Python:

import multiprocessing  
import time

def square_numbers():
    for i in range(5):
        print(f"Square of {i}: {i**2}")
        time.sleep(2)  # Simulate a time-consuming task

def cube_numbers():
    for i in range(5):
        print(f"Cube of {i}: {i**3}")
        time.sleep(2)  # Simulate a time-consuming task

if __name__ == "__main__":
    # Create processes for each function
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()

    # Start both processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    finished_time = time.time() - start_time
    print(f"Time taken with multiprocessing: {finished_time} seconds")