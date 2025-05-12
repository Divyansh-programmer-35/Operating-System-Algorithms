import threading
import time
import random

N = 5
THINKING = 0
HUNGRY = 1
EATING = 2

state = [THINKING] * N
mutex = threading.Semaphore(1)
semaphores = [threading.Semaphore(0) for _ in range(N)]

def left(i): return (i + N - 1) % N
def right(i): return (i + 1) % N

def test(i):
    if state[i] == HUNGRY and state[left(i)] != EATING and state[right(i)] != EATING:
        state[i] = EATING
        semaphores[i].release()

def take_forks(i):
    with mutex:
        state[i] = HUNGRY
        print(f"Philosopher {i} is HUNGRY.")
        test(i)
    semaphores[i].acquire()

def put_forks(i):
    with mutex:
        state[i] = THINKING
        print(f"Philosopher {i} puts down forks and starts THINKING.")
        test(left(i))
        test(right(i))

def philosopher(i):
    while True:
        time.sleep(random.uniform(1, 3))
        take_forks(i)
        print(f"Philosopher {i} is EATING.")
        time.sleep(random.uniform(1, 2))
        put_forks(i)

threads = []
for i in range(N):
    t = threading.Thread(target=philosopher, args=(i,))
    threads.append(t)
    t.start()