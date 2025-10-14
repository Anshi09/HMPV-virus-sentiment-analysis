// #include <stdio.h>
// #include <string.h>

// void vulnerable_function(char *input) {
//     char buffer[10];
//     strcpy(buffer, input);
//     printf("Buffer content: %s\n", buffer);
// }

// int main() {
//     char input[100];
//     printf("Enter your input: ");
//     fgets(input, sizeof(input), stdin);
//     input[strcspn(input, "\n")] = 0;  

//     vulnerable_function(input);

//     return 0;
// }
#include <stdio.h>
#include <string.h>

// Safe function to prevent buffer overflow
void safe_function(char *input) {
    char buffer[10];
    // Using strncpy to limit copy size and prevent overflow
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[9] = '\0'; // Explicit null termination
    printf("Buffer content: %s\n", buffer);
}

int main() {
    char input[100];
    printf("Enter your input: ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;  // Remove newline

    // Call the safe function
    safe_function(input);

    return 0;
}