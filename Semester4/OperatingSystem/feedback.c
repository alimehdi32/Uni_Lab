#include <stdio.h>

int main() {
    int n, i;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], rt[n], wt[n], tat[n], pid[n];

    for(i = 0; i < n; i++) {
        pid[i] = i + 1;
        printf("Enter AT and BT for P%d: ", i+1);
        scanf("%d %d", &at[i], &bt[i]);
        rt[i] = bt[i];
    }

    int tq1, tq2;
    printf("Enter Time Quantum for Q1: ");
    scanf("%d", &tq1);
    printf("Enter Time Quantum for Q2: ");
    scanf("%d", &tq2);

    int time = 0, completed = 0;

    printf("\nGantt Chart:\n|");

    int q1_done[n], q2_done[n];

    for(i = 0; i < n; i++) {
        q1_done[i] = 0;
        q2_done[i] = 0;
    }

    while(completed < n) {
        int executed = 0;

        for(i = 0; i < n; i++) {
            if(at[i] <= time && rt[i] > 0 && q1_done[i] == 0) {
                executed = 1;
                printf(" P%d |", pid[i]);

                if(rt[i] > tq1) {
                    time += tq1;
                    rt[i] -= tq1;
                    q1_done[i] = 1;
                } else {
                    time += rt[i];
                    rt[i] = 0;
                    wt[i] = time - bt[i] - at[i];
                    if(wt[i] < 0) wt[i] = 0;
                    completed++;
                }
            }
        }

        for(i = 0; i < n; i++) {
            if(at[i] <= time && rt[i] > 0 && q1_done[i] == 1 && q2_done[i] == 0) {
                executed = 1;
                printf(" P%d |", pid[i]);

                if(rt[i] > tq2) {
                    time += tq2;
                    rt[i] -= tq2;
                    q2_done[i] = 1;
                } else {
                    time += rt[i];
                    rt[i] = 0;
                    wt[i] = time - bt[i] - at[i];
                    if(wt[i] < 0) wt[i] = 0;
                    completed++;
                }
            }
        }

        for(i = 0; i < n; i++) {
            if(at[i] <= time && rt[i] > 0 && q2_done[i] == 1) {
                executed = 1;
                printf(" P%d |", pid[i]);

                time += rt[i];
                rt[i] = 0;
                wt[i] = time - bt[i] - at[i];
                if(wt[i] < 0) wt[i] = 0;
                completed++;
            }
        }

        if(executed == 0)
            time++;
    }

    printf("\n0");
    for(i = 1; i <= time; i++)
        printf(" %d", i);

    float avg_wt = 0, avg_tat = 0;

    printf("\n\nProcess AT BT WT TAT\n");
    for(i = 0; i < n; i++) {
        tat[i] = wt[i] + bt[i];
        avg_wt += wt[i];
        avg_tat += tat[i];
        printf("P%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], wt[i], tat[i]);
    }

    printf("\nAvg WT: %.2f\n", avg_wt/n);
    printf("Avg TAT: %.2f\n", avg_tat/n);

    return 0;
}