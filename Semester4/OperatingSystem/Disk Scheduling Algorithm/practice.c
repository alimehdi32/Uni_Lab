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

void sstf(int req[], int n, int head, int DISK_SIZE){
    int sorted[n];
    for(int i = 0; i < n; i++) {
        sorted[i] = req[i];
    }
    sort(sorted, n);
     
}

int main() {
    int req[MAX], n, head, direction, choice, DISK_SIZE;
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