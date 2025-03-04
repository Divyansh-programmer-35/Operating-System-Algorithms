def round_robin(processes, arrival_time, burst_time, quantum):
    n = len(processes)
    remaining_time = burst_time[:]  
    waiting_time = [0] * n  
    turnaround_time = [0] * n  
    completion_time = [0] * n  

    time = 0  
    queue = []  
    index = 0  
    queue_sequence = []  

    while index < n or queue:
        while index < n and arrival_time[index] <= time:
            queue.append(index)
            index += 1
        
        if queue:
            current = queue.pop(0)  
            queue_sequence.append(processes[current])  
            
            if remaining_time[current] > quantum:
                time += quantum
                remaining_time[current] -= quantum
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

    print("\nProcess Table:")
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<12}{'Waiting Time':<15}{'Turnaround Time'}")
    for i in range(n):
        print(f"{processes[i]:<10}{arrival_time[i]:<15}{burst_time[i]:<12}{waiting_time[i]:<15}{turnaround_time[i]}")


    print("\nQueue Formation (Order of Execution):")
    print(" → ".join(queue_sequence))


processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 2, 3]  
burst_time = [5, 8, 12, 6]  
quantum = 3  

round_robin(processes, arrival_time, burst_time, quantum)
