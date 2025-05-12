import threading
import time

NUM_PHILOSOPHERS = 5
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

def philosopher(i):
    left_fork = forks[i]
    right_fork = forks[(i + 1) % NUM_PHILOSOPHERS]
    while True:
        print(f"Philosopher {i} is thinking.")
        time.sleep(1)  
        print(f"Philosopher {i} is hungry.")
        
        left_fork.acquire()
        print(f"Philosopher {i} picked up left fork {i}.")
        time.sleep(0.1)  
        right_fork.acquire()
        print(f"Philosopher {i} picked up right fork {(i + 1) % NUM_PHILOSOPHERS}.")
        print(f"Philosopher {i} is eating.")
        time.sleep(2)

        left_fork.release()
        right_fork.release()
        print(f"Philosopher {i} put down both forks.")

for i in range(NUM_PHILOSOPHERS):
    threading.Thread(target=philosopher, args=(i,), daemon=True).start()

while True:
    time.sleep(1)
