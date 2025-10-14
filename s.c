#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool SQL(const char* input) {
    if (strstr(input, "'") != NULL)
        return true;
    if (strstr(input, "--") != NULL)
        return true;
    if (strstr(input, ";") != NULL)
        return true;
    return false;
}

int main() {
    char username[100], password[100];

    printf("Enter username: ");
    scanf("%99s", username);

    printf("Enter password: ");
    scanf("%99s", password);

    if (SQL(username) || SQL(password)) {
        printf("SQL Injection attempt detected\n");
    } else {
        printf("No SQL Injection attempt detected\n");
    }

    return 0;
}