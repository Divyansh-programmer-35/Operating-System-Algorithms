import java.util.Scanner;

class Process {
    int pid; 
    int arrivalTime;
    int burstTime;
    int completionTime;
    int turnaroundTime;
    int waitingTime;
}

public class FCFS {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter number of processes: ");
            int n = sc.nextInt();
            
            Process[] processes = new Process[n];
            
            for (int i = 0; i < n; i++) {
                processes[i] = new Process();
                System.out.println("Enter arrival time and burst time for process " + (i + 1) + ":");
                processes[i].pid = i + 1;
                processes[i].arrivalTime = sc.nextInt();
                processes[i].burstTime = sc.nextInt();
            }
            
            // Sorting processes by arrival time
            for (int i = 0; i < n - 1; i++) {
                for (int j = 0; j < n - i - 1; j++) {
                    if (processes[j].arrivalTime > processes[j + 1].arrivalTime) {
                        Process temp = processes[j];
                        processes[j] = processes[j + 1];
                        processes[j + 1] = temp;
                    }
                }
            }
            
            // Calculating completion, turnaround, and waiting times
            int currentTime = 0;
            for (int i = 0; i < n; i++) {
                if (currentTime < processes[i].arrivalTime) {
                    currentTime = processes[i].arrivalTime;
                }
                processes[i].completionTime = currentTime + processes[i].burstTime;
                processes[i].turnaroundTime = processes[i].completionTime - processes[i].arrivalTime;
                processes[i].waitingTime = processes[i].turnaroundTime - processes[i].burstTime;
                currentTime = processes[i].completionTime;
            }
            
            // Printing the results
            System.out.println("\nProcess	Arrival Time	Burst Time	Completion Time	Turnaround Time	Waiting Time");
            for (Process p : processes) {
                System.out.println(p.pid + "\t" + p.arrivalTime + "\t\t" + p.burstTime + "\t\t" + p.completionTime + "\t\t" + p.turnaroundTime + "\t\t" + p.waitingTime);
            }
        }
    }
}
