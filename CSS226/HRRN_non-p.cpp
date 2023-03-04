#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct process {
    int pid;
    int arrival;
    int burst;
    int waiting;
};

bool compareArrivalTime(process p1, process p2) {
    return p1.arrival < p2.arrival;
}

bool compareResponseRatio(process p1, process p2) {
    return ((p1.burst + (p1.waiting - p1.arrival)) / p1.burst) > ((p2.burst + (p2.waiting - p2.arrival)) / p2.burst);
}

int main() {
    vector<process> processes;
    processes.push_back({0, 0, 10});
    processes.push_back({1, 2, 5});
    processes.push_back({2, 4, 3});
    processes.push_back({3, 5, 4});

    sort(processes.begin(), processes.end(), compareArrivalTime);

    int n = processes.size();
    int current_time = 0;
    vector<int> completion_time(n), waiting_time(n);

    for (int i = 0; i < n; i++) {
        waiting_time[i] = current_time - processes[i].arrival;
        current_time += processes[i].burst;
        completion_time[i] = current_time;
    }

    for (int i = 0; i < n; i++) {
        processes[i].waiting = waiting_time[i];
    }

    sort(processes.begin(), processes.end(), compareResponseRatio);

    current_time = 0;

    for (int i = 0; i < n; i++) {
        waiting_time[i] = current_time - processes[i].arrival;
        current_time += processes[i].burst;
        completion_time[i] = current_time;
    }

    for (int i = 0; i < n; i++) {
        cout << "Process " << processes[i].pid << " Completion Time: " << completion_time[i] << " Waiting Time: " << waiting_time[i] << endl;
    }

    return 0;
}
