#include <iostream>
#include <string>
#include <stdlib.h>
#include <time.h>

#include "Fighter.h"

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main() {
	
	Fighter* ptr_fighter = new Fighter("Josh", 100, 100);
	cout << ptr_fighter->showName() << endl;

	Fighter player1;
	player1.setName("Dom");
	//player1.setHealth(100);
	//player1.setPower(100);
	cout << "Name: " << player1.showName() << endl;
	cout << "Health: " << player1.showHealth() << endl;
	cout << "Power: " << player1.showPower() << endl;

	Fighter player2;
	player2.setName("Dom Jr");
	//player2.setHealth(100);
	//player2.setPower(100);
	cout << "Name: " << player2.showName() << endl;
	cout << "Health: " << player2.showHealth() << endl;
	cout << "Power: " << player2.showPower() << endl;

	srand(time(NULL));

	cout << "--------THE BRAWL STARTS---------" << endl;


	player1.kick(player2);

	cout << "Name: " << player1.showName() << endl;
	cout << "Health: " << player1.showHealth() << endl;
	cout << "Power: " << player1.showPower() << endl;
	cout << "Name: " << player2.showName() << endl;
	cout << "Health: " << player2.showHealth() << endl;
	cout << "Power: " << player2.showPower() << endl;

	//cout << "Enter your name: ";
//string user_name;5
//cin >> user_name;

//Fighter test(user_name, 90, 40);
//cout << "Name: " << test.showName() << endl;
//cout << "Health: " << test.showHealth() << endl;
//cout << "Power: " << test.showPower() << endl;

////delete object:
//test.~Fighter();

//cout << "Name: " << test.showName() << endl;
//cout << "Health: " << test.showHealth() << endl;
//cout << "Power: " << test.showPower() << endl;

	
	//while ((player1.showHealth() > 0) && (player2.showHealth() > 0)) {
	//	//player 1 turn
	//	cout << "Enter your move: 1 - punch, 2 - guard" << endl;
	//	int choice;
	//	cin >> choice;

	//	//player 2 turn
	//	int rand_num = (rand() % 2) + 1;

	//	//outcomes
	//	if (choice == 1 && rand_num == 1) {
	//		player1.punch();
	//		player2.damage();
	//		player2.punch();
	//		player1.damage();
	//	}
	//	else if (choice == 1 && rand_num == 2){
	//		player1.punch();
	//		player2.block();
	//	}
	//	else if (choice == 2 && rand_num == 1) {
	//		player1.block();
	//		player2.punch();
	//	}
	//	else if (choice == 2 && rand_num == 2) {
	//		player1.block();
	//		player2.block();
	//	}
	//	cout << "Name: " << player1.showName() << endl;
	//	cout << "Health: " << player1.showHealth() << endl;
	//	cout << "Power: " << player1.showPower() << endl;

	//	cout << "Name: " << player2.showName() << endl;
	//	cout << "Health: " << player2.showHealth() << endl;
	//	cout << "Power: " << player2.showPower() << endl;
	//}

	//Display winner/loser
	/*if (player1.showHealth() > 0) {
		cout << player1.showName() << " won!" << endl;
	}
	else if (player2.showHealth() > 0) {
		cout << player2.showName() << " won!" << endl;
	}
	else {
		cout << "Draw!" << endl;
	}*/

	return 0;
}