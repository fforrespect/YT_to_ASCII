#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <math.h>

#include "all_frames.h"

char *strings_fp = "../resources/strings/frame_strings.txt";
const char *delimiter = "ARBITRARY_DELIMITER";
double fps = 30;

void drawAllFrames();

void drawAllFrames() {
    FILE *strings_file = fopen(strings_fp, "r");
    if (!strings_file) {
        perror("Failed to open file");
        return;
    }

    // Find the file size
    fseek(strings_file, 0, SEEK_END);
    long file_size = ftell(strings_file);
    fseek(strings_file, 0, SEEK_SET);

    // Dynamically allocate buffer
    char *buffer = malloc(file_size + 1);
    if (!buffer) {
        perror("Failed to allocate memory");
        fclose(strings_file);
        return;
    }

    fread(buffer, file_size, 1, strings_file);
    buffer[file_size] = '\0'; // Null-terminate the string

    char *frame_start = buffer;
    char *frame_end;

    double frame_time = 1.0 / fps;
    struct timespec next_frame_time;
    clock_gettime(CLOCK_REALTIME, &next_frame_time);

    while ((frame_end = strstr(frame_start, delimiter)) != NULL) {
        *frame_end = '\0'; // Split the string
        system("clear");
        printf("%s\n", frame_start);

        // Sleep logic
        next_frame_time.tv_sec += (int)frame_time;
        next_frame_time.tv_nsec += (int)((frame_time - (int)frame_time) * 1e9);
        if (next_frame_time.tv_nsec >= 1e9) {
            next_frame_time.tv_sec++;
            next_frame_time.tv_nsec -= 1e9;
        }

        struct timespec current_time;
        clock_gettime(CLOCK_REALTIME, &current_time);

        if ((next_frame_time.tv_sec > current_time.tv_sec) ||
            (next_frame_time.tv_sec == current_time.tv_sec && next_frame_time.tv_nsec > current_time.tv_nsec)) {
            struct timespec sleep_time;
            sleep_time.tv_sec = next_frame_time.tv_sec - current_time.tv_sec;
            sleep_time.tv_nsec = next_frame_time.tv_nsec - current_time.tv_nsec;
            nanosleep(&sleep_time, NULL);
        }

        frame_start = frame_end + strlen(delimiter);
    }


    // Handle the last frame if there's any
    if (*frame_start) {
        system("clear");
        printf("%s\n", frame_start);
    }

    free(buffer);
    fclose(strings_file);
}

