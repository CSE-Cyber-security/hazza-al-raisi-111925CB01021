#include <stdio.h>

int main(void) {
    int choice;
    double num1, num2;

    printf("===== Simple Calculator =====\n");
    printf("1. Addition (+)\n");
    printf("2. Subtraction (-)\n");
    printf("3. Multiplication (*)\n");
    printf("4. Division (/)\n");

    printf("Enter your choice (1-4): ");
    if (scanf("%d", &choice) != 1) {
        printf("Invalid input!\n");
        return 1;
    }

    printf("Enter two numbers: ");
    if (scanf("%lf %lf", &num1, &num2) != 2) {
        printf("Invalid numbers!\n");
        return 1;
    }

    switch (choice) {
        case 1:
            printf("Result = %.2f\n", num1 + num2);
            break;

        case 2:
            printf("Result = %.2f\n", num1 - num2);
            break;

        case 3:
            printf("Result = %.2f\n", num1 * num2);
            break;

        case 4:
            if (num2 == 0) {
                printf("Error: Division by zero!\n");
            } else {
                printf("Result = %.2f\n", num1 / num2);
            }
            break;

        default:
            printf("Invalid choice!\n");
    }

    return 0;
}
