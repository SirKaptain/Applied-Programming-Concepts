#include "Fighter.h"

Fighter::Fighter() {
	name = "Tom";
	health = 100;
	power = 100;
}

Fighter::Fighter(string in_name, int in_health, int in_power) {
	name = in_name;
	health = in_health;
	power = in_power;
}
void Fighter::setName(string username) {
	name = username;
}
string Fighter::showName() {
	return name;
}

void Fighter::setHealth(int newHealth) {
	health = newHealth;
}
int Fighter::showHealth() {
	return health;
}

void Fighter::setPower(int newPower) {
	power = newPower;
}
int Fighter::showPower() {
	return power;
}

void Fighter::punch() {
	power = power - 10;
}

void Fighter::damage() {
	health = health - 8;
}

void Fighter::block() {
	power = power + 5;
}

void Fighter::kick(Fighter &opp) {
	power = power - 20;
	opp.health = opp.health - 10;
}

Fighter::~Fighter() {

}