#include <iostream>
#include <array>
using namespace std;

// Character Values
const int NUM_CHARS = 8; // number of characters
array<string, NUM_CHARS> name = { "Mario", "Luigi","Peach", "Toad", "Yoshi", "D.K.", "Wario", "Bowser" };
array<double, NUM_CHARS> weight = { 1.2, 1.0, 0.9, 0.9, 0.7, 2.0, 1.8, 2.3 };
array<int, NUM_CHARS> speed = { 68, 68, 70, 70, 70, 66, 66, 68 };
array<double, NUM_CHARS> acceleration = { 3.5, 3, 4.5, 4.5, 5, 1, 1, 2.5 };

// Menu Options
const int SINGLE_PLAYER = 1;
const int MULTI_PLAYER = 2;
const int CO_OP = 3;
const int CC_50 = 1;
const int CC_100 = 2;
const int CC_150 = 3;

// This function asks the user to select a game mode and returns the choice as an integer
int getMode()
{
    cout << "       Please Select a mode" << endl;
    cout << SINGLE_PLAYER << ".     Single Player Grand Prix" << endl;
    cout << MULTI_PLAYER << ".     Multiplayer Grand Prix" << endl;
    cout << CO_OP << ".     Co-op Grand Prix" << endl;
    int m; // mode choice
    cin >> m;
    // validate input
    while (cin.fail() || m < SINGLE_PLAYER || m > CO_OP) {
        cout << "Invalid input. Please enter a number between " << SINGLE_PLAYER << " and " << CO_OP << "." << endl;
        cin.clear(); // clear error flags
        cin.ignore(1000, '\n'); // ignore any remaining characters in the buffer
        cin >> m; // try again
    }
    return m;
}

// This function asks the user to select a character and returns the choice as a string
string getPlayer()
{
    cout << "       Please Select a character" << endl;
    string wei; // weight category
    for (int i = 0; i < NUM_CHARS; i++)
    {
        if (weight[i] < 1)
        {
            wei = " Light";
        }
        else if (weight[i] <= 1.75)
        {
            wei = " Medium";
        }
        else
        {
            wei = " Heavy";
        }
        cout << i + 1 << ".   " << name[i] << wei << " Weight" << endl;
    }
    int p; // character choice
    cin >> p;
    // validate input
    while (cin.fail() || p < 1 || p > NUM_CHARS) {
        cout << "Invalid input. Please enter a number between 1 and " << NUM_CHARS << "." << endl;
        cin.clear(); // clear error flags
        cin.ignore(1000, '\n'); // ignore any remaining characters in the buffer
        cin >> p; // try again
    }
    return name[p - 1]; // return the corresponding character name
}

// This function asks the user to select a game difficulty and returns the choice as an integer
int getDifficulty()
{
    cout << "       Please Select Game Difficulty" << endl;
    cout << CC_50 << ".                 50CC" << endl;
    cout << CC_100 << ".                100CC" << endl;
    cout << CC_150 << ".                150CC" << endl;
    int d; // difficulty choice
    cin >> d;
    // validate input
    while (cin.fail() || d < CC_50 || d > CC_150) {
        cout << "Invalid input. Please enter a number between " << CC_50 << " and " << CC_150 << "." << endl;
        cin.clear(); // clear error flags
        cin.ignore(1000, '\n'); // ignore any remaining characters in the buffer
        cin >> d; // try again
    }
    return d;
}

int main()
{
    cout << "       Hello" << endl;
    int difficulty = getDifficulty(); // get the difficulty from the user
    int mode = getMode(); // get the mode from the user
    string player1 = getPlayer(); // get the first player from the user
    string player2; // second player
    if (mode == MULTI_PLAYER || mode == CO_OP)
    {
        player2 = getPlayer(); // get the second player from the user
    }

    return 0;
}
