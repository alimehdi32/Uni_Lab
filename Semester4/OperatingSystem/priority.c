#include <stdio.h>

int main() {
    int n, i;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], pr[n], pid[n];

    for(i = 0; i < n; i++) {
        pid[i] = i + 1;
        printf("Enter AT, BT, Priority for P%d: ", i + 1);
        scanf("%d %d %d", &at[i], &bt[i], &pr[i]);
    }

    printf("\n===== Non-Preemptive Priority Scheduling =====\n");

    int completed = 0, time = 0, min, idx;
    int wt1[n], tat1[n], done[n];

    for(i = 0; i < n; i++) done[i] = 0;

    float avg_wt1 = 0, avg_tat1 = 0;

    printf("\nGantt Chart:\n|");

    while(completed < n) {
        min = 9999;
        idx = -1;

        for(i = 0; i < n; i++) {
            if(at[i] <= time && done[i] == 0 && pr[i] < min) {
                min = pr[i];
                idx = i;
            }
        }

        if(idx == -1) {
            time++;
            continue;
        }

        printf(" P%d |", pid[idx]);

        wt1[idx] = time - at[idx];
        time += bt[idx];
        tat1[idx] = wt1[idx] + bt[idx];

        avg_wt1 += wt1[idx];
        avg_tat1 += tat1[idx];

        done[idx] = 1;
        completed++;
    }

    printf("\n0");
    for(i = 1; i <= time; i++) printf(" %d", i);

    printf("\n\nProcess AT BT PR WT TAT\n");
    for(i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], pr[i], wt1[i], tat1[i]);

    printf("\nAvg WT: %.2f\n", avg_wt1/n);
    printf("Avg TAT: %.2f\n", avg_tat1/n);

    printf("\n===== Preemptive Priority Scheduling =====\n");

    int rt[n], wt2[n], tat2[n];
    int completed2 = 0, time2 = 0;

    for(i = 0; i < n; i++) rt[i] = bt[i];

    float avg_wt2 = 0, avg_tat2 = 0;

    printf("\nGantt Chart:\n|");

    while(completed2 < n) {
        min = 9999;
        idx = -1;

        for(i = 0; i < n; i++) {
            if(at[i] <= time2 && rt[i] > 0 && pr[i] < min) {
                min = pr[i];
                idx = i;
            }
        }

        if(idx == -1) {
            time2++;
            continue;
        }

        printf(" P%d |", pid[idx]);

        rt[idx]--;
        time2++;

        if(rt[idx] == 0) {
            completed2++;
            wt2[idx] = time2 - bt[idx] - at[idx];
            if(wt2[idx] < 0) wt2[idx] = 0;
            tat2[idx] = wt2[idx] + bt[idx];
        }
    }

    printf("\n0");
    for(i = 1; i <= time2; i++) printf(" %d", i);

    printf("\n\nProcess AT BT PR WT TAT\n");
    for(i = 0; i < n; i++) {
        avg_wt2 += wt2[i];
        avg_tat2 += tat2[i];
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], pr[i], wt2[i], tat2[i]);
    }

    printf("\nAvg WT: %.2f\n", avg_wt2/n);
    printf("Avg TAT: %.2f\n", avg_tat2/n);

    return 0;
}