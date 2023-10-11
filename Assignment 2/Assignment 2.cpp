// Assignment 2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

using namespace std;

// Charater Values
string name[8] = { "Mario", "Luigi","Peach", "Toad", "Yoshi", "D.K.", "Wario", "Bowser" };
double weight[8] = { 1.2, 1.0, 0.9, 0.9, 0.7, 2.0, 1.8, 2.3 };
int speed[8] = { 68, 68, 70, 70, 70, 66, 66, 68 };
double acceleration[8] = { 3.5, 3, 4.5, 4.5, 5, 1, 1, 2.5 };

void getMode(int m)
{
    cout << "       Please Select a mode" << endl;
    cout << "1.     Single Player Grand Prix" << endl;
    cout << "2.     Multiplayer Grand Prix" << endl;
    cout << "3.     Co-op Grand Prix" << endl;
    cin >> m;
}

void getPlayer(string player)
{
    cout << "       Please Select a charater" << endl;
    string wei;
    for (int i = 0; i < 8; i++)
    {
        if (weight[i] < 1)
        {
            wei = " Light";
        }
        if (1<= weight[i] && weight[i] <= 1.75)
        {
            wei = " Medium";
        }    
        if (weight[i] < 1.75)
        {
            wei = " Heavy";
        }
        cout << i + 1 << "   " << name[i] << wei << " Weight" << endl;
    }
    cin >> player;
}

void getDifficulty(int d)
{
    cout << "       Please Select Game Difficulty" << endl;
    cout << "1.                 50CC" << endl;
    cout << "2.                100CC" << endl;
    cout << "3.                150CC" << endl;
    cin >> d;
}

int main()
{
    cout << "       Hello" << endl;
    int* difficulty;
    int* mode;
    string* player1;
    string* player2;

    getDifficulty(*difficulty);
    getMode(*mode);
    if (*mode == 2) 
    {
        getPlayer(*player1);
        getPlayer(*player2);

    }
    else
        getPlayer(*player1);

    
    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
