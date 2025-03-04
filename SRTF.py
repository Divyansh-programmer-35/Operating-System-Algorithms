import heapq

def srtf_scheduling(processes):
    n = len(processes)
    processes.sort(key=lambda x: x[1])  

    remaining_time = {pid: burst for pid, arrival, burst in processes}
    original_burst_time = {pid: burst for pid, arrival, burst in processes}  
    completion_time = {}
    turnaround_time = {}
    waiting_time = {}
    
    current_time = 0
    completed = 0
    min_heap = []
    i = 0
    
    while completed < n:
        while i < n and processes[i][1] <= current_time:
            heapq.heappush(min_heap, (remaining_time[processes[i][0]], processes[i][0], processes[i][1]))
            i += 1
        
        if min_heap:
            burst, pid, arrival = heapq.heappop(min_heap)
            remaining_time[pid] -= 1
            current_time += 1
            
            if remaining_time[pid] == 0:
                completion_time[pid] = current_time
                turnaround_time[pid] = completion_time[pid] - arrival
                waiting_time[pid] = turnaround_time[pid] - original_burst_time[pid]  
                completed += 1
            else:
                heapq.heappush(min_heap, (remaining_time[pid], pid, arrival))
        else:
            current_time += 1
    
    total_waiting_time = sum(waiting_time.values())
    total_turnaround_time = sum(turnaround_time.values())
    total_completion_time = sum(completion_time.values())
    
    print("\nProcess\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for pid, arrival, burst in processes:
        print(f"{pid}\t{arrival}\t\t{burst}\t\t{completion_time[pid]}\t\t{turnaround_time[pid]}\t\t{waiting_time[pid]}")
    
    print("\nAverage Completion Time:", total_completion_time / n)
    print("Average Turnaround Time:", total_turnaround_time / n)
    print("Average Waiting Time:", total_waiting_time / n)


processes = [(i + 1, *map(int, input(f"Enter arrival time and burst time for process {i + 1}: ").split())) for i in range(int(input("Enter number of processes: ")))]
srtf_scheduling(processes)