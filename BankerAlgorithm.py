
import numpy as np

def is_safe(available, max_demand, allocation, num_processes, num_resources):
    work, finish, sequence = available[:], [False] * num_processes, []
    while len(sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i] and all(max_demand[i][j] - allocation[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocation[i][j] for j in range(num_resources)]
                sequence.append(i)
                finish[i] = True
                found = True
                break
        if not found:
            return False, []
    return True, sequence

def request_resources(process_id, request, available, max_demand, allocation, num_processes, num_resources):
    if any(request[j] > max_demand[process_id][j] - allocation[process_id][j] for j in range(num_resources)):
        return "Request denied"
    
    if any(request[j] > available[j] for j in range(num_resources)):
        return "Request denied"
    
    allocation[process_id] = [allocation[process_id][j] + request[j] for j in range(num_resources)]
    
    safe, sequence = is_safe(available, max_demand, allocation, num_processes, num_resources)
    return "Request granted" if safe else "Request denied"


num_processes, num_resources = 4, 3
available = [3, 3, 0]
max = [[4,3,1], [2,1,4], [1,3,3], [5,4,1]]
allocation = [[1,0,1], [1,1,2], [1,0,3], [2,0,0]]

safe, sequence = is_safe(available, max, allocation, num_processes, num_resources)
if safe:
    print("Safe sequence:", sequence)
else:
    print("System is in an unsafe state!")

