// Assignment2.cpp 
#include <iostream>

using namespace std;

// Charater Values
string name[8] = { "Mario", "Luigi","Peach", "Toad", "Yoshi", "D.K.", "Wario", "Bowser" };
double weight[8] = { 1.2, 1.0, 0.9, 0.9, 0.7, 2.0, 1.8, 2.3 };
int speed[8] = { 68, 68, 70, 70, 70, 66, 66, 68 };
double acceleration[8] = { 3.5, 3, 4.5, 4.5, 5, 1, 1, 2.5 };

void getMode(int& m)
{
	cout << " Please Select a mode" << endl;
	cout << "1. Single Player Grand Prix" << endl;
	cout << "2. Multiplayer Grand Prix" << endl;
	cout << "3. Co-op Grand Prix" << endl;
	cin >> m;
	if (m == 1)
		cout << "Single Player Grand Prix" << endl;
	if (m == 2)
		cout << "Multiplayer Grand Prix" << endl;
	if (m == 3)
		cout << "Co-op Grand Prix" << endl;
}
void getPlayer(string& player)
{
	cout << " Please Select a charater" << endl;
	string wei;
	for (int i = 0; i < 8; i++)
	{
		if (weight[i] < 1)
		{
			wei = " Light";
		}
		if (1 <= weight[i] && weight[i] <= 1.75)
		{
			wei = " Medium";
		}
		if (weight[i] < 1.75)
		{
			wei = " Heavy";
		}
		cout << i + 1 << " " << name[i] << wei << " Weight" << endl;
	}
	int select;
	cin >> select;
	if (select < 0 || select > 7)
	{
		cout << "error Value out of range" << endl;
	}
	else
	{
		player = name[select - 1];
	}

}
void getDifficulty(int d)
{
	cout << " Please Select Game Difficulty" << endl;
	cout << "1. 50CC" << endl;
	cout << "2. 100CC" << endl;
	cout << "3. 150CC" << endl;
	cin >> d;
	if (d == 1)
	{
		cout << "50CC Selected" << endl;
	}
	if (d == 2)
	{
		cout << "100CC Selected" << endl;
	}
	if (d == 3)
	{
		cout << "150CC Selected" << endl;
	}
}
int main()
{
	cout << " Welcome" << endl;

	int difficulty =0;
	int* ptrD;
	ptrD = &difficulty;

	int mode =0;
	int* ptrM;
	ptrM = &mode;

	string player1 ="";
	string* ptrP1;
	ptrP1= &player1;

	string player2 = "";
	string* ptrP2;
	ptrP2= &player2;

	getDifficulty(*ptrD);
	getMode(*ptrM);
	if (*ptrM >= 2)
	{
		cout << " Player 1" << endl;
		getPlayer(*ptrP1);
		cout << " Player 2" << endl;
		getPlayer(*ptrP2);
		cout << " Player 1 Selected: " << player1 << endl;
		cout << " Player 2 Selected: " << player2 << endl;
	}
	else
	{
		getPlayer(*ptrP1);
		cout << " Player Selected: " << player1 << endl;
	}
	return 0;
}

