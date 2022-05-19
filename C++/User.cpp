#include "User.hpp"


	//constructor (initial value)
	User::User(){
		first_name = "First Name";
		last_name = "Last Name";
		id = "W00000000";
	}
	//Constructor (inputed values)
	User::User(string first_name, string last_name, string id){
		this->first_name = first_name;
		this->last_name = last_name;
		this->id = id;
	}

	void User::set_first_name(string new_first_name){
		first_name = new_first_name;
	}
	string User::show_first_name(){
		return first_name;
	}
	
	void User::set_last_name(string new_last_name){
		last_name = new_last_name;
	}
	string User::show_last_name(){
		return last_name;
	}

	void User::set_id(string new_id){
		id = new_id;
	}
	string User::show_id(){
		return id;
	}

	//Destructor
	User::~User(){

	}