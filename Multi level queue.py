# ROUND ROBIN SCHEDULING
def round_robin(processes, time_quantum):
    time = 0
    completed_processes = []
    ready_queue = []
    total_processes = len(processes)

    processes.sort(key=lambda p: p['arrival'])

    while len(completed_processes) < total_processes:
        for process in processes:
            if process not in ready_queue and process not in completed_processes:
                if process['arrival'] <= time:
                    ready_queue.append(process)

        if len(ready_queue) > 0:
            current_process = ready_queue.pop(0)

            if 'start' not in current_process:
                current_process['start'] = time

            execution_time = min(current_process['remaining'], time_quantum)
            time += execution_time
            current_process['remaining'] -= execution_time

            for process in processes:
                if process not in ready_queue and process not in completed_processes:
                    if process['arrival'] > current_process['arrival'] and process['arrival'] <= time:
                        ready_queue.append(process)

            if current_process['remaining'] == 0:
                current_process['completion'] = time
                completed_processes.append(current_process)
            else:
                ready_queue.append(current_process)
        else:
            time += 1  

    return completed_processes, time

# FCFS SCHEDULING
def fcfs(processes, start_time):
    processes.sort(key=lambda p: p['arrival'])
    current_time = start_time
    completed_processes = []

    for process in processes:
        if current_time < process['arrival']:
            current_time = process['arrival']

        process['start'] = current_time
        current_time += process['burst']
        process['completion'] = current_time

        completed_processes.append(process)

    return completed_processes


all_processes = [
    {'pid': 1, 'arrival': 0, 'burst': 5},
    {'pid': 2, 'arrival': 1, 'burst': 3},
    {'pid': 3, 'arrival': 2, 'burst': 8},
    {'pid': 4, 'arrival': 3, 'burst': 6},
    {'pid': 5, 'arrival': 4, 'burst': 4},
]


queue1_processes = []
queue2_processes = []

for process in all_processes:
    process['remaining'] = process['burst']
    if process['burst'] <= 5:
        process['queue'] = 1
        queue1_processes.append(process.copy())
    else:
        process['queue'] = 2
        queue2_processes.append(process.copy())


time_quantum = 3
completed_queue1, end_time_queue1 = round_robin(queue1_processes, time_quantum)
completed_queue2 = fcfs(queue2_processes, end_time_queue1)


all_completed = completed_queue1 + completed_queue2
all_completed.sort(key=lambda p: p['pid'])


print("PID\tArrival\tBurst\tQueue\tStart\tCompletion\tTurnaround\tWaiting")
print()
for process in all_completed:
    turnaround_time = process['completion'] - process['arrival']
    waiting_time = turnaround_time - process['burst']
    print(f"{process['pid']}\t{process['arrival']}\t{process['burst']}\t{process['queue']}\t"
          f"{process['start']}\t{process['completion']}\t\t{turnaround_time}\t\t{waiting_time}")
    print()


