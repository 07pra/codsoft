#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator with the current time
    std::srand(static_cast<unsigned int>(std::time(nullptr))); 

    // Generate a random number between 1 and 100
    int randomNumber = std::rand() % 100 + 1;

    int userGuess;
    int numGuesses = 0;

    std::cout << "Welcome to the Number Guessing Game!\n";
    
    do {
        std::cout << "Guess a number between 1 and 100: ";
        std::cin >> userGuess;
        
        numGuesses++;

        if (userGuess < randomNumber) {
            std::cout << "Too low! Try again.\n";
        } else if (userGuess > randomNumber) {
            std::cout << "Too high! Try again.\n";
        } else {
            std::cout << "Congratulations! You guessed the number " << randomNumber << " in " << numGuesses << " guesses.\n";
        }
    } while (userGuess != randomNumber);

    return 0;
}
