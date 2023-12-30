#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <pthread.h>

#include "audio.h"
#include "all_frames.h"

// Thread function prototypes
void *audioThreadFunc(void *arg);
void *framesThreadFunc(void *arg);

int main() {
    char *pythonFile = "ProcessAll.py";
    int status;
    pthread_t audioThread, framesThread;

    printf("Processing audio and video...\n");
    pid_t pid = fork();

    if (pid == 0) {
        // Child process
        execlp("python3", "python3", pythonFile, (char *) NULL);
        exit(EXIT_FAILURE);
    } else if (pid > 0) {
        // Parent process
        waitpid(pid, &status, 0);
        printf("Done processing audio and video\n");

        // Create threads
        pthread_create(&audioThread, NULL, audioThreadFunc, NULL);
        pthread_create(&framesThread, NULL, framesThreadFunc, NULL);

        // Wait for threads to finish
        pthread_join(audioThread, NULL);
        pthread_join(framesThread, NULL);

    } else {
        // Fork failed
        printf("Failed to fork a process\n");
    }

    return 0;
}

void *audioThreadFunc(void *arg) {
    playAudio();
    return NULL;
}

void *framesThreadFunc(void *arg) {
    drawAllFrames();
    return NULL;
}
