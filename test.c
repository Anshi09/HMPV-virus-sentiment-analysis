#include <pthread.h>
#include <stdio.h>

#define NUM_ITERATIONS 50000

// Shared Counter
int counter = 0;
// Thread Function (Without Synchronization)
void* increment_counter(void* arg) {
    for (int i = 0; i < NUM_ITERATIONS; ++i) {
        counter++;
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;

    // Create two threads
    pthread_create(&thread1, NULL, increment_counter, NULL);
    pthread_create(&thread2, NULL, increment_counter, NULL);

    // Wait for both threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("Expected Final Counter: %d\n", NUM_ITERATIONS * 2);
    printf("Actual Final Counter: %d\n", counter);

    return 0;
}