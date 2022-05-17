#include "Instructor.h"


	//constructor (initial value)
	Instructor::Instructor() : User(){
        
    }
	//Constructor (inputed values)
	Instructor::Instructor(string first_name, string last_name, string id) : User(first_name, last_name, id){

	}

	void Instructor::print_schedule(){
        cout << "Print Schedule for Instructor!" << endl;
    }
    void Instructor::print_classlist(){
        cout << "Print Classlist for Instructor!" << endl;
    }
    void Instructor::search_course(){
        cout << "Search course for Instructor!" << endl;
    }

    //Deconstructor
    Instructor::~Instructor(){

    }