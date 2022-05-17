#pragma once
#include <string>
using std::string;
#include <iostream>
using namespace std;

class User
{
	//attributes
protected:
	string first_name;
	string last_name;
	string id;

	//methods
public:
	//constructor (initial value)
	User();
	User(string first_name, string last_name, string id);

	//Destructor
	~User();

	void set_first_name(string new_first_name);
	string show_first_name();
	
	void set_last_name(string new_last_name);
	string show_last_name();

	void set_id(string new_id);
	string show_id();
};
