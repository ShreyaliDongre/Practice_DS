###  Multi-threading and Multi-processing in Python with threadpool and processpool executors:
#In Python, you can use the concurrent.futures module to manage threads and processes more easily.
# The ThreadPoolExecutor is used for multi-threading, while the ProcessPoolExecutor is used for multi-processing. 
# Here's how you can use both:
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def print_numbers(number):
    time.sleep(1)  # Simulate a time-consuming task
    return f"Number:{number} "

def square_number(number):
    time.sleep(1)  # Simulate a time-consuming task
    return f"Square of {number}: {number**2} "

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    print("Threading Example:")
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(print_numbers, numbers)
    for result in results:
        print(result)
    
    # ---------------------------------------------------------------------------
    print("\nProcessing Example:")
    with ProcessPoolExecutor(max_workers=4) as executor:
        res = executor.map(square_number, numbers)
    for r in res:
        print(r)
