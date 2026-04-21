#include <stdio.h>

int main() {
    int n, i, tq;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], rt[n], wt[n], tat[n], pid[n];

    for(i = 0; i < n; i++) {
        pid[i] = i + 1;
        printf("Enter AT and BT for P%d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        rt[i] = bt[i];
    }

    printf("Enter Time Quantum: ");
    scanf("%d", &tq);

    int time = 0, completed = 0;

    printf("\nGantt Chart:\n|");

    while(completed < n) {
        int done = 1;

        for(i = 0; i < n; i++) {
            if(at[i] <= time && rt[i] > 0) {
                done = 0;

                printf(" P%d |", pid[i]);

                if(rt[i] > tq) {
                    time += tq;
                    rt[i] -= tq;
                } else {
                    time += rt[i];
                    wt[i] = time - bt[i] - at[i];
                    if(wt[i] < 0) wt[i] = 0;
                    rt[i] = 0;
                    completed++;
                }
            }
        }

        if(done == 1)
            time++;
    }

    printf("\n0");
    for(i = 1; i <= time; i++)
        printf(" %d", i);

    float avg_wt = 0, avg_tat = 0;

    printf("\n\nProcess AT BT WT TAT\n");
    for(i = 0; i < n; i++) {
        tat[i] = bt[i] + wt[i];
        avg_wt += wt[i];
        avg_tat += tat[i];
        printf("P%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], wt[i], tat[i]);
    }

    printf("\nAvg WT: %.2f\n", avg_wt/n);
    printf("Avg TAT: %.2f\n", avg_tat/n);

    return 0;
}