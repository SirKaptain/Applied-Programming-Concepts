#include "Admin.h"


	//constructor (initial value)
	Admin::Admin() : User(){
        first_name = "Admin First";
        last_name = "Admin Last";
        id = "333333";
    }
	//Constructor (inputed values)
	Admin::Admin(string first_name, string last_name, string id) : User(first_name, last_name, id){
	}

	void Admin::add_course(){
        cout << "Add Course for Admin!" << endl;
    }
    void Admin::remove_course(){
        cout << "Remove Course for Admin!" << endl;
    }
    void Admin::add_user(){
        cout << "Add User for Admin!" << endl;
    }
    void Admin::remove_user(){
        cout << "Remove User for Admin!" << endl;
    }
    void Admin::add_student_to_course(){
        cout << "Add Student to Course for Admin!" << endl;
    }
    void Admin::remove_student_from_course(){
        cout << "Remove Student from Course for Admin!" << endl;
    }
    void Admin::search_roster(){
        cout << "Search Roster for Admin!" << endl;
    }
    void Admin::print_roster(){
        cout << "Print Roster for Admin!" << endl;
    }
    void Admin::search_course(){
        cout << "Search Course for Admin!" << endl;
    }
    void Admin::print_course(){
        cout << "Print Course for Admin!" << endl;
    }

    //Deconstructor
    Admin::~Admin(){

    }