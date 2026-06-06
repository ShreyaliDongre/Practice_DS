<img width="846" height="465" alt="image" src="https://github.com/user-attachments/assets/bc733a81-9a96-463f-8614-b0a4012056f4" />

# Python Multithreading and Multiprocessing

## 1. Program

A **Program** is a sequence of instructions written in a programming language.

Examples:
- Python
- C++
- Java

A program is **passive**, meaning it stays stored until executed.

### Example
```python
print("Hello")
```

This code is a **program**.

---

## 2. Process

A **Process** is a **program in execution**.

When a program runs, the Operating System creates a process.

### A Process Contains
- Memory
- Resources
- Program Counter
- Stack and Heap
- Process ID (PID)

### Characteristics of a Process
- Independent execution
- Separate memory space
- Heavyweight compared to threads
- One process can contain multiple threads

### Python Example
```python
import os

print("Process ID:", os.getpid())
```

Running this creates a **process**.

---

## 3. Thread

A **Thread** is the **smallest unit of execution inside a process**.

Threads belong to a process and share its resources.

### Characteristics of Threads
- Lightweight
- Faster than processes
- Share memory and resources
- Used for concurrent execution

### Simple Analogy
- **Process = House**
- **Threads = People inside the house performing tasks**

Same process, shared resources.

---

## Process vs Thread

| Feature | Process | Thread |
|----------|----------|--------|
| Definition | Program in execution | Small execution unit inside a process |
| Memory | Separate | Shared |
| Speed | Slower | Faster |
| Communication | IPC required | Shared memory |
| Resource Usage | High | Low |
| Failure | Usually isolated | Can affect entire process |

---

# Python Multithreading

**Multithreading** means running multiple threads inside the same process.

Best suited for:
- File handling
- Network requests
- Downloading
- I/O operations

Python provides the `threading` module.

## Example

```python
import threading
import time

def task():
    for i in range(3):
        print("Thread running")
        time.sleep(1)

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")
```

### Output (Sample)

```python
Thread running
Thread running
Thread running
...
Done
```

Both threads execute **concurrently**.

---

## Global Interpreter Lock (GIL)

Python has a mechanism called **GIL (Global Interpreter Lock)**.

### GIL Means
- Multiple threads cannot execute Python bytecode simultaneously in CPython
- Multithreading works best for **I/O-bound tasks**
- Not ideal for CPU-intensive work

---

# Python Multiprocessing

**Multiprocessing** means running multiple independent processes.

Each process:
- Has separate memory
- Executes independently
- Can use multiple CPU cores

Best suited for:
- Heavy calculations
- Data processing
- CPU-bound tasks
- Machine Learning workloads

Python provides the `multiprocessing` module.

## Example

```python
from multiprocessing import Process
import os

def task():
    print("Process ID:", os.getpid())

p1 = Process(target=task)
p2 = Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()
```

### Output (Sample)

```python
Process ID: 1234
Process ID: 5678
```

Different PIDs indicate different processes.

---

# Real-Life Examples

## Process Examples
1. Web Browser
2. VS Code
3. Music Player
4. Python Application

Each application is usually a separate process.

---

## Thread Examples

### Browser Example
**Process:** Chrome Browser

**Threads:**
- UI Thread
- Rendering Thread
- Download Thread
- Audio Thread

---

### Restaurant Example

**Process:** Restaurant

**Threads:**
- Taking orders
- Cooking
- Billing
- Serving

Same process performing multiple tasks.

---

# Summary

## Program
- Written code
- Stored on disk
- Passive

## Process
- Program in execution
- Has its own memory and resources

## Thread
- Smallest execution unit
- Shares process resources

## Multithreading
- Multiple threads
- Best for I/O-bound tasks

## Multiprocessing
- Multiple processes
- Best for CPU-bound tasks

---

## Key Difference

| Multithreading | Multiprocessing |
|---------------|----------------|
| Shared memory | Separate memory |
| Faster creation | Higher overhead |
| Best for I/O tasks | Best for CPU tasks |
| Limited by GIL | Uses multiple CPU cores |
