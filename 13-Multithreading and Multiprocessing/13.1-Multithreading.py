## Multithreading
## When to use multithreading
## I/O - bound tasks : Tasks that spend more time waiting for I/O operations(eg: File operations , network requests)
## Concurrent execution : When you want to improve the throughput of your application by preforming mulitple operations concurrently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f"Letter:{letter}")

## create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
t1.start()
t2.start()

## Wait for entire threads to complete
t1.join()
t2.join()

print_numbers()
print_letter()
finished_time = time.time() - t
print(finished_time)
