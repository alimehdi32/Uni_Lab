#include <stdio.h>
#include <stdbool.h>

void display(int frames[], int n) {
    for (int i = 0; i < n; i++) {
        if (frames[i] == -1) printf(" - ");
        else printf(" %d ", frames[i]);
    }
    printf("\n");
}

int findOptimal(int pages[], int frames[], int n, int m, int index) {
    int res = -1, farthest = index;
    for (int i = 0; i < m; i++) {
        int j;
        for (j = index; j < n; j++) {
            if (frames[i] == pages[j]) {
                if (j > farthest) {
                    farthest = j;
                    res = i;
                }
                break;
            }
        }
        if (j == n) return i;
    }
    return (res == -1) ? 0 : res;
}

int findLRU_MRU(int time[], int n, bool findLRU) {
    int pos = 0, target = time[0];
    for (int i = 1; i < n; i++) {
        if (findLRU) {
            if (time[i] < target) { target = time[i]; pos = i; }
        } else {
            if (time[i] > target) { target = time[i]; pos = i; }
        }
    }
    return pos;
}

void solve(int pages[], int n, int m, int mode) {
    int frames[m], time[m], faults = 0, pointer = 0;
    for (int i = 0; i < m; i++) frames[i] = -1;

    printf("\nString | Frame Contents\n-----------------------\n");
    for (int i = 0; i < n; i++) {
        printf("  %d    |", pages[i]);
        bool found = false;
        for (int j = 0; j < m; j++) {
            if (frames[j] == pages[i]) {
                found = true;
                time[j] = i; // Update access time for LRU/MRU
                break;
            }
        }

        if (!found) {
            if (mode == 1) { // FIFO
                frames[pointer] = pages[i];
                pointer = (pointer + 1) % m;
            } else if (mode == 2) { // Optimal
                int pos = findOptimal(pages, frames, n, m, i + 1);
                frames[pos] = pages[i];
            } else { // LRU (mode 3) or MRU (mode 4)
                int empty = -1;
                for(int k=0; k<m; k++) if(frames[k] == -1) { empty = k; break; }
                
                if (empty != -1) frames[empty] = pages[i], time[empty] = i;
                else {
                    int pos = findLRU_MRU(time, m, (mode == 3));
                    frames[pos] = pages[i];
                    time[pos] = i;
                }
            }
            faults++;
            display(frames, m);
        } else {
            printf("  Hit\n");
        }
    }
    printf("-----------------------\nTotal Page Faults: %d\n", faults);
}

int main() {
    int n, m, choice;
    printf("Ali Mehdi - 24BCS008\n");
    printf("Enter number of pages: ");
    scanf("%d", &n);
    int pages[n];
    printf("Enter reference string: ");
    for (int i = 0; i < n; i++) scanf("%d", &pages[i]);
    printf("Enter number of frames: ");
    scanf("%d", &m);

    do {
        printf("\n--- Page Replacement Menu ---\n1. FIFO\n2. Optimal\n3. LRU\n4. MRU\n5. Exit\nChoice: ");
        scanf("%d", &choice);
        if (choice >= 1 && choice <= 4) solve(pages, n, m, choice);
    } while (choice != 5);

    return 0;
}