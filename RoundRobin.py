def round_robin(processes, arrival_time, burst_time, quantum):
    n = len(processes)
    sorted_processes = sorted(zip(arrival_time, burst_time, processes))
    arrival_time, burst_time, processes = zip(*sorted_processes)
    
    remaining_time = list(burst_time)  
    waiting_time = [0] * n  
    turnaround_time = [0] * n  
    completion_time = [0] * n  

    time = 0  
    queue = []  
    index = 0  
    queue_sequence = []  
    in_queue = [False] * n  

    while index < n or queue:
        while index < n and arrival_time[index] <= time:
            queue.append(index)
            in_queue[index] = True  
            index += 1
        
        if queue:
            current = queue.pop(0)  
            queue_sequence.append(processes[current])  
            
            if remaining_time[current] > quantum:
                time += quantum
                remaining_time[current] -= quantum
                while index < n and arrival_time[index] <= time:
                    if not in_queue[index]:  
                        queue.append(index)
                        in_queue[index] = True
                    index += 1
                queue.append(current)  
            else:
                time += remaining_time[current]
                completion_time[current] = time
                remaining_time[current] = 0 
        else:
            time = arrival_time[index]  

    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    print("\nProcess Table:")
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<12}{'Waiting Time':<15}{'Turnaround Time'}")
    for i in range(n):
        print(f"{processes[i]:<10}{arrival_time[i]:<15}{burst_time[i]:<12}{waiting_time[i]:<15}{turnaround_time[i]}")

    print("\nQueue Formation (Order of Execution):")
    print(" → ".join(queue_sequence))

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 2, 1, 3]  
burst_time = [5, 7, 6, 8]  
quantum = 4  

round_robin(processes, arrival_time, burst_time, quantum)
