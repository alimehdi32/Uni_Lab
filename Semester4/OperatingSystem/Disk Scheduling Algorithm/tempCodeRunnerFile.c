#include <stdio.h>
#include <stdlib.h>

#define MAX 100
//#define DISK_SIZE 200

// Sort function
void sort(int arr[], int n) {
    for(int i = 0; i < n-1; i++) {
        for(int j = i+1; j < n; j++) {
            if(arr[i] > arr[j]) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

// FCFS
void fcfs(int req[], int n, int head, int DISK_SIZE) {
    int total = 0;

    printf("Seek Sequence: %d", head);

    for(int i = 0; i < n; i++) {
        printf(" -> %d", req[i]);
        total += abs(req[i] - head);
        head = req[i];
    }

    printf("\nTotal Head Movement (FCFS): %d\n", total);
}

// SSTF
void sstf(int req[], int n, int head, int DISK_SIZE) {
    int visited[MAX] = {0}, total = 0;

    printf("Seek Sequence: %d", head);

    for(int i = 0; i < n; i++) {
        int min = 1e9, index = -1;

        for(int j = 0; j < n; j++) {
            if(!visited[j]) {
                int dist = abs(req[j] - head);
                if(dist < min) {
                    min = dist;
                    index = j;
                }
            }
        }

        printf(" -> %d", req[index]);

        total += min;
        head = req[index];
        visited[index] = 1;
    }

    printf("\nTotal Head Movement (SSTF): %d\n", total);
}

// SCAN
void scan(int req[], int n, int head, int direction, int DISK_SIZE) {
    int total = 0;
    int left[MAX], right[MAX], l = 0, r = 0;

    printf("Seek Sequence: %d", head);

    for(int i = 0; i < n; i++) {
        if(req[i] < head)
            left[l++] = req[i];
        else
            right[r++] = req[i];
    }

    sort(left, l);
    sort(right, r);

    if(direction == 1) {
        for(int i = 0; i < r; i++) {
            printf(" -> %d", right[i]);
            total += abs(right[i] - head);
            head = right[i];
        }

        printf(" -> %d", DISK_SIZE - 1);
        total += abs((DISK_SIZE - 1) - head);
        head = DISK_SIZE - 1;

        for(int i = l-1; i >= 0; i--) {
            printf(" -> %d", left[i]);
            total += abs(left[i] - head);
            head = left[i];
        }
    } else {
        for(int i = l-1; i >= 0; i--) {
            printf(" -> %d", left[i]);
            total += abs(left[i] - head);
            head = left[i];
        }

        printf(" -> 0");
        total += abs(head - 0);
        head = 0;

        for(int i = 0; i < r; i++) {
            printf(" -> %d", right[i]);
            total += abs(right[i] - head);
            head = right[i];
        }
    }

    printf("\nTotal Head Movement (SCAN): %d\n", total);
}

// C-SCAN
void cscan(int req[], int n, int head, int direction, int DISK_SIZE) {
    int total = 0;
    int left[MAX], right[MAX], l = 0, r = 0;

    printf("Seek Sequence: %d", head);

    for(int i = 0; i < n; i++) {
        if(req[i] < head)
            left[l++] = req[i];
        else
            right[r++] = req[i];
    }

    sort(left, l);
    sort(right, r);

    if(direction == 1) {
        for(int i = 0; i < r; i++) {
            printf(" -> %d", right[i]);
            total += abs(right[i] - head);
            head = right[i];
        }

        printf(" -> %d -> 0", DISK_SIZE - 1);
        total += abs((DISK_SIZE - 1) - head);
        total += (DISK_SIZE - 1);
        head = 0;

        for(int i = 0; i < l; i++) {
            printf(" -> %d", left[i]);
            total += abs(left[i] - head);
            head = left[i];
        }
    }

    printf("\nTotal Head Movement (C-SCAN): %d\n", total);
}

// LOOK
void look(int req[], int n, int head, int direction, int DISK_SIZE) {
    int total = 0;
    int left[MAX], right[MAX], l = 0, r = 0;

    printf("Seek Sequence: %d", head);

    for(int i = 0; i < n; i++) {
        if(req[i] < head)
            left[l++] = req[i];
        else
            right[r++] = req[i];
    }

    sort(left, l);
    sort(right, r);

    if(direction == 1) {
        for(int i = 0; i < r; i++) {
            printf(" -> %d", right[i]);
            total += abs(right[i] - head);
            head = right[i];
        }

        for(int i = l-1; i >= 0; i--) {
            printf(" -> %d", left[i]);
            total += abs(left[i] - head);
            head = left[i];
        }
    }

    printf("\nTotal Head Movement (LOOK): %d\n", total);
}

// C-LOOK
void clook(int req[], int n, int head, int direction, int DISK_SIZE) {
    int total = 0;
    int left[MAX], right[MAX], l = 0, r = 0;

    printf("Seek Sequence: %d", head);

    for(int i = 0; i < n; i++) {
        if(req[i] < head)
            left[l++] = req[i];
        else
            right[r++] = req[i];
    }

    sort(left, l);
    sort(right, r);

    if(direction == 1) {
        for(int i = 0; i < r; i++) {
            printf(" -> %d", right[i]);
            total += abs(right[i] - head);
            head = right[i];
        }

        if(l > 0) {
            printf(" -> %d", left[0]);
            total += abs(head - left[0]);
            head = left[0];
        }

        for(int i = 1; i < l; i++) {
            printf(" -> %d", left[i]);
            total += abs(left[i] - head);
            head = left[i];
        }
    }

    printf("\nTotal Head Movement (C-LOOK): %d\n", total);
}

// MAIN
int main() {
    int req[MAX], n, head, direction, choice, DISK_SIZE;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter Total Disk Cylinders: ");
    scanf("%d", &DISK_SIZE);

    printf("Enter number of requests: ");
    scanf("%d", &n);

    printf("Enter request queue:\n");
    for(int i = 0; i < n; i++)
        scanf("%d", &req[i]);

    printf("Enter current head position: ");
    scanf("%d", &head);

    printf("Enter direction (0 = Left, 1 = Right): ");
    scanf("%d", &direction);

    do {
        printf("\n--- Disk Scheduling Menu ---\n");
        printf("1. FCFS\n2. SSTF\n3. SCAN\n4. C-SCAN\n5. LOOK\n6. C-LOOK\n7. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1: fcfs(req, n, head, DISK_SIZE); break;
            case 2: sstf(req, n, head, DISK_SIZE); break;
            case 3: scan(req, n, head, direction, DISK_SIZE); break;
            case 4: cscan(req, n, head, direction, DISK_SIZE); break;
            case 5: look(req, n, head, direction, DISK_SIZE); break;
            case 6: clook(req, n, head, direction, DISK_SIZE); break;
            case 7: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }

    } while(choice != 7);

    return 0;
}