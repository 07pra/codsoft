#include <iostream>
using namespace std;

// Function to display the game board
void displayBoard(char board[3][3]) {
    cout << "  1 2 3\n";
    for (int i = 0; i < 3; i++) {
        cout << i + 1 << " ";
        for (int j = 0; j < 3; j++) {
            cout << board[i][j] << " ";
        }
        cout << "\n";
    }
}

// Function to check if a player has won
bool checkWin(char board[3][3], char player) {
    // Check rows, columns, and diagonals
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
            return true;
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player)
            return true;
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
        return true;
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
        return true;
    return false;
}

// Function to check if the game is a draw
bool checkDraw(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ')
                return false;  // Empty cell found, game is not a draw
        }
    }
    return true;  // All cells are filled, game is a draw
}

int main() {
    char board[3][3] = { {' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '} };
    char currentPlayer = 'X';
    bool gameOver = false;

    cout << "TIC-TAC-TOE GAME\n";
    displayBoard(board);

    while (!gameOver) {
        int row, col;

        // Get player's move
        cout << "Player " << currentPlayer << ", enter your move (row column): ";
        cin >> row >> col;

        // Check if the move is valid
        if (row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1][col - 1] != ' ') {
            cout << "Invalid move. Try again.\n";
            continue;
        }

        // Update the board
        board[row - 1][col - 1] = currentPlayer;
        displayBoard(board);

        // Check for win or draw
        if (checkWin(board, currentPlayer)) {
            cout << "Player " << currentPlayer << " wins!\n";
            gameOver = true;
        } else if (checkDraw(board)) {
            cout << "It's a draw!\n";
            gameOver = true;
        }

        // Switch players
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
