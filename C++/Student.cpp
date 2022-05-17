#include "Student.h"


	//constructor (initial value)
	Student::Student() : User(){
        first_name = "Student First";
        last_name = "Student Last";
        id = "111111";
    }
	//Constructor (inputed values)
	Student::Student(string first_name, string last_name, string id) : User(first_name, last_name, id){
	}

	void Student::search_course(){
        cout << "Search course for Student!" << endl;
    }
    void Student::add_course(){
        cout << "Add Course for Student!" << endl;
    }
    void Student::drop_course(){
        cout << "Drop Course for Student!" << endl;
    }
    void Student::print_schedule(){
        cout << "Print Schedule for Student!" << endl;
    }

    //Deconstructor
    Student::~Student(){

    }