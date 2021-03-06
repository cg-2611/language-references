#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    // dynamic sized strings:
    // can be declared as either:
    // char *string;
    // char string[];

    // example:
    char *dynamic_string = malloc((16 + 1) * sizeof(*dynamic_string)); // allocate memory for a string of size 16 + 1
    strcpy(dynamic_string, "This is a string"); // copy a string to the memory

    printf("Dynamic string value: %s\n", dynamic_string);
    printf("Dynamic string length: %lu\n", strlen(dynamic_string));

    // can also use realloc instead of free and malloc

    // deallocate memory
    free(dynamic_string);
    dynamic_string = NULL;

    dynamic_string = malloc((32 + 1) * sizeof(*dynamic_string)); // allocate memory for a string of size 32 + 1
    strcpy(dynamic_string, "This is a bigger string"); // copy a larger string to the memory

    printf("Dynamic string value: %s\n", dynamic_string);
    printf("Dynamic string length: %lu\n", strlen(dynamic_string));

    // deallocate memory
    free(dynamic_string);
    dynamic_string = NULL;

    return 0;
}
