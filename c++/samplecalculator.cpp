#include <iostream>

int main() {
    double num1, num2;
    char operation;

    std::cout << "Welcome to the Basic Calculator!\n";

    // Input the two numbers
    std::cout << "Enter the first number: ";
    std::cin >> num1;

    std::cout << "Enter the second number: ";
    std::cin >> num2;

    // Choose the operation
    std::cout << "Choose an operation (+, -, *, /): ";
    std::cin >> operation;

    double result;

    // Perform the selected operation
    switch (operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                std::cout << "Error: Division by zero is not allowed.\n";
                return 1; // Exit with an error code
            }
            break;
        default:
            std::cout << "Error: Invalid operation.\n";
            return 1; // Exit with an error code
    }

    // Display the result
    std::cout << "Result: " << result << std::endl;

    return 0;
}
