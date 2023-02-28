processes = [
    (0, 0, 10),  # process 0: arrival time 0, burst time 10
    (1, 2, 5),   # process 1: arrival time 2, burst time 5
    (2, 4, 3),   # process 2: arrival time 4, burst time 3
    (3, 5, 4)    # process 3: arrival time 5, burst time 4
]

response_ratio = {}
remaining_time = {}
completion_time = {}
waiting_time = {}
current_time = 0
total_time = 0

# calculate response ratio and remaining time for each process
for i in range(len(processes)):
    pid, arrival, burst = processes[i]
    response_ratio[pid] = (total_time - arrival + burst) / burst
    remaining_time[pid] = burst

# schedule processes in preemptive manner
while remaining_time:
    # select process with highest response ratio
    pid = max(response_ratio, key=response_ratio.get)
    arrival, burst = processes[pid][1:]

    # check if process is preempted
    if arrival > current_time:
        current_time = arrival

    # update remaining time and response ratio for selected process
    remaining_time[pid] -= 1
    response_ratio[pid] = (total_time - arrival + remaining_time[pid] + 1) / (remaining_time[pid] + 1)

    if remaining_time[pid] == 0:
        # process has completed
        completion_time[pid] = current_time + 1
        waiting_time[pid] = current_time - arrival - burst + 1
        total_time += 1
        current_time += 1

        # remove process from dictionaries
        del remaining_time[pid]
        del response_ratio[pid]
    else:
        # process has not completed
        total_time += 1
        current_time += 1

# print completion time and waiting time for each process
for pid in range(len(completion_time)):
    print("Process", pid, "Completion Time:", completion_time[pid], "Waiting Time:", waiting_time[pid])
