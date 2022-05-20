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
	
	void User::set_last_name(string new_last_name){
		last_name = new_last_name;
	}

	void User::set_id(string new_id){
		id = new_id;
	}

	void User::show_info(){
		cout << first_name << endl;
		cout << last_name << endl;
		cout << id << endl;
	}

	void User::edit_info(){
		string new_info;
		int user_input;
		
		while (true){
			cout << "What information would you like to edit?:" << endl;
			cout << "First Name(1)   Last Name(2)" << endl;
			cout << "ID(3)           Back(0)" << endl;
			cout << "Input: ";
			cin >> user_input;

			if (user_input == 1){
				cout << "What would you like to change your first name to?" << endl;
                cout << "New First Name: ";
				cin >> new_info;
				first_name = new_info;
			}
                
            else if (user_input == 2){
				cout << "What would you like to change your Last name to?" << endl;
                cout << "New Last Name: ";
				cin >> new_info;
				last_name = new_info;
			}

			else if (user_input == 3){
				cout << "What would you like to change your id to?" << endl;
                cout << "New ID: ";
				cin >> new_info;
				id = new_info;
			}
			else if (user_input == 0){
				break;
			}
            else{
				cout << "Invalid Option" << endl;
			}
		}
	}

	//Destructor
	User::~User(){

	}