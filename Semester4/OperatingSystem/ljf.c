#include <stdio.h>

int main() {
    int n, i;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], wt[n], tat[n], pid[n], done[n];

    for(i = 0; i < n; i++) {
        pid[i] = i + 1;
        done[i] = 0;
        printf("Enter AT and BT for P%d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
    }

    int completed = 0, time = 0;
    float avg_wt = 0, avg_tat = 0;

    printf("\nGantt Chart:\n|");

    while(completed < n) {
        int idx = -1;
        int max_bt = -1;

        for(i = 0; i < n; i++) {
            if(at[i] <= time && done[i] == 0 && bt[i] > max_bt) {
                max_bt = bt[i];
                idx = i;
            }
        }

        if(idx == -1) {
            time++;
            continue;
        }

        printf(" P%d |", pid[idx]);

        wt[idx] = time - at[idx];
        if(wt[idx] < 0) wt[idx] = 0;

        time += bt[idx];

        tat[idx] = wt[idx] + bt[idx];

        avg_wt += wt[idx];
        avg_tat += tat[idx];

        done[idx] = 1;
        completed++;
    }

    printf("\n0");
    for(i = 1; i <= time; i++)
        printf(" %d", i);

    printf("\n\nProcess AT BT WT TAT\n");
    for(i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], wt[i], tat[i]);

    printf("\nAvg WT: %.2f\n", avg_wt/n);
    printf("Avg TAT: %.2f\n", avg_tat/n);

    return 0;
}