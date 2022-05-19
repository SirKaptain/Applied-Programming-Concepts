#include <iostream>


#include "Student.hpp"
#include "Instructor.hpp"
#include "Admin.hpp"


using std::cin;
using std::cout;
using std::endl;


int main() {
	int user_input;
	cout << "Welcome to Leopard Web!" << endl;
	do{
		cout << "Choose an option:" << endl;
		cout << "Student(1)" << endl;
		cout << "Instructor(2)" << endl;
		cout << "Admin(3)" << endl;
		cout << "Exit(0)" << endl;
		cout << "Input:";
		cin >> user_input;

		if (user_input == 1){
			Student* ptr_student = new Student("Dom", "Ioime", "W00397674");
			do{
				cout << "Choose an option:" << endl;
				cout << "Add Course(1)" << endl;
				cout << "Drop Course(2)" << endl;
				cout << "Print Schedule(3)" << endl;
				cout << "Search Course(4)" << endl;
				cout << "Exit(0)" << endl;
				cout << "Input:";
				cin >> user_input;
				if (user_input == 1){
					ptr_student->add_course();
				}
				else if (user_input == 2){
					ptr_student->drop_course();
				}
				else if (user_input == 3){
					ptr_student->print_schedule();
				}
				else if (user_input == 4){
					ptr_student->search_course();
				}
				else if (user_input == 0){
					continue;
				}
				else{
					cout << "Invalid Option!";
				}
			} while (user_input != 0);
			ptr_student->~Student();
		}
		else if (user_input == 2){
			Instructor* ptr_instructor = new Instructor("Ahmed", "Hassebo", "W00111111");
			do{
				cout << "Choose an option:" << endl;
				cout << "Print Schedule(1)" << endl;
				cout << "Print Classlist(2)" << endl;
				cout << "Search Course(3)" << endl;
				cout << "Exit(0)" << endl;
				cout << "Input:";
				cin >> user_input;
				if (user_input == 1){
					ptr_instructor->print_schedule();
				}
				else if (user_input == 2){
					ptr_instructor->print_classlist();
				}
				else if (user_input == 3){
					ptr_instructor->search_course();
				}
				else if (user_input == 0){
					continue;
				}
				else{
					cout << "Invalid Option!";
				}
			}while (user_input != 0);
			ptr_instructor->~Instructor();
		}
		else if (user_input == 3){
			Admin* ptr_admin = new Admin("Mark", "Thompson", "W00999999");
			do{
				cout << "Choose an option:" << endl;
				cout << "Add Course(1)" << endl;
				cout << "Remove Course(2)" << endl;
				cout << "Add User(3)" << endl;
				cout << "Remove User(4)" << endl;
				cout << "Add a Student to a Course(5)" << endl;
				cout << "Remove a Student from a Course(6)" << endl;
				cout << "Search Roster(7)" << endl;
				cout << "Print Roster(8)" << endl;
				cout << "Search Course(9)" << endl;
				cout << "Print Course(10)" << endl;
				cout << "Exit(0)" << endl;
				cout << "Input:";
				cin >> user_input;
				if (user_input == 1){
					ptr_admin->add_course();
				}
				else if (user_input == 2){
					ptr_admin->remove_course();
				}
				else if (user_input == 3){
					ptr_admin->add_user();
				}
				else if (user_input == 4){
					ptr_admin->remove_user();
				}
				else if (user_input == 5){
					ptr_admin->add_student_to_course();
				}
				else if (user_input == 6){
					ptr_admin->remove_student_from_course();
				}
				else if (user_input == 7){
					ptr_admin->search_roster();
				}
				else if (user_input == 8){
					ptr_admin->print_roster();
				}
				else if (user_input == 9){
					ptr_admin->search_course();
				}
				else if (user_input == 10){
					ptr_admin->print_course();
				}
				else if (user_input == 0){
					continue;
				}
				else{
					cout << "Invalid Option!";
				}
			}while (user_input != 0);
			ptr_admin->~Admin();
		}
		else if (user_input == 0){
			cout << "Have a nice day!";
			break;
		}
		else {
			cout << "Invalid Option!" << endl;
		}

	}while(user_input != 0);
	
	return 0;
}