#pragma once
#include <string>
using std::string;

class Fighter
{
	//attribute (Data)
	string name;
	int health;
	int power;

	//method (What it can do)
public:
	//constructor (initial value)
	Fighter();
	Fighter(string in_name, int in_health, int in_power);

	//Destructor
	~Fighter();

	void setName(string username);
	string showName();
	
	void setHealth(int newHealth);
	int showHealth();

	void setPower(int newPower);
	int showPower();

	void punch();

	void damage();

	void block();

	void kick(Fighter &opp);
};

