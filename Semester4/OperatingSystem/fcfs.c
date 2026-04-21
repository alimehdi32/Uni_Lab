#include <stdio.h>

int main() {
    int n, i, j;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], wt[n], tat[n], pid[n];

    for(i = 0; i < n; i++) {
        pid[i] = i + 1;
        printf("Enter arrival time and burst time for P%d: ", i+1);
        scanf("%d %d", &at[i], &bt[i]);
    }

    for(i = 0; i < n-1; i++) {
        for(j = i+1; j < n; j++) {
            if(at[i] > at[j]) {
                int t;
                t = at[i]; at[i] = at[j]; at[j] = t;
                t = bt[i]; bt[i] = bt[j]; bt[j] = t;
                t = pid[i]; pid[i] = pid[j]; pid[j] = t;
            }
        }
    }

    int time = 0;
    float avg_wt = 0, avg_tat = 0;

    for(i = 0; i < n; i++) {
        if(time < at[i]) time = at[i];
        wt[i] = time - at[i];
        time += bt[i];
        tat[i] = wt[i] + bt[i];
        avg_wt += wt[i];
        avg_tat += tat[i];
    }

    printf("\nProcess AT BT WT TAT\n");
    for(i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], wt[i], tat[i]);

    printf("\nAvg WT: %.2f\n", avg_wt/n);
    printf("Avg TAT: %.2f\n", avg_tat/n);

    printf("\nGantt Chart:\n|");
    time = 0;
    for(i = 0; i < n; i++) {
        if(time < at[i]) time = at[i];
        printf(" P%d |", pid[i]);
        time += bt[i];
    }

    printf("\n0");
    time = 0;
    for(i = 0; i < n; i++) {
        if(time < at[i]) time = at[i];
        time += bt[i];
        printf(" %d", time);
    }

    return 0;
}