#include <iostream>

using namespace std;

#include "Student.hpp"
#include "Instructor.hpp"
#include "Admin.hpp"

int main() {
	int user_input = 1;
	cout << "Welcome to Leopard Web!" << endl;
	while(user_input != 0){
		cout << "Choose an option:" << endl;
		cout << "Student(1)		Instructor(2)" << endl;
		cout << "Admin(3)		Exit(0)" << endl;
		cout << "Input: ";
		cin >> user_input;

		if (user_input == 1){
			Student* ptr_student = new Student("Dom", "Ioime", "W00397674");
			while (user_input != 0){
				cout << "Choose an option:" << endl;
				cout << "Add Course(1)			Drop Course(2)" << endl;
				cout << "Print Schedule(3)		Search Course(4)" << endl;
				cout << "Show Info(5)			Edit Info(6)" << endl;
				cout << "Exit(0)" << endl;
				cout << "Input: ";
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
				else if (user_input == 5){
					ptr_student->show_info();
				}
				else if (user_input == 6){
					ptr_student->edit_info();
				}
				else if (user_input == 0){
					continue;
				}
				else{
					cout << "Invalid Option!";
				}
			}
			ptr_student->~Student();
		}
		else if (user_input == 2){
			Instructor* ptr_instructor = new Instructor("Ahmed", "Hassebo", "W00111111");
			while (user_input != 0){
				cout << "Choose an option:" << endl;
				cout << "Print Schedule(1)		Print Classlist(2)" << endl;
				cout << "Search Course(3)		Show Info(4)" << endl;
				cout << "Edit Info(5)			Exit(0)" << endl;
				cout << "Input: ";
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
				else if (user_input == 4){
					ptr_instructor->show_info();
				}
				else if (user_input == 5){
					ptr_instructor->edit_info();
				}
				else if (user_input == 0){
					continue;
				}
				else{
					cout << "Invalid Option!";
				}
			}
			ptr_instructor->~Instructor();
		}
		else if (user_input == 3){
			Admin* ptr_admin = new Admin("Mark", "Thompson", "W00999999");
			while (user_input != 0){
				cout << "Choose an option:" << endl;
				cout << "Add Course(1)	Remove Course(2)	Add User(3)	Remove User(4)" << endl;
				cout << "Add a Student to a Course(5)	Remove a Student from a Course(6)" << endl;
				cout << "Search Roster(7)	Print Roster(8)		Search Course(9)	Print Course(10)" << endl;
				cout << "Show Info(11)	Edit Info(12)	Exit(0)" << endl;
				cout << "Input: ";
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
				else if (user_input == 11){
					ptr_admin->show_info();
				}
				else if (user_input == 12){
					ptr_admin->edit_info();
				}
				else if (user_input == 0){
					continue;
				}
				else{
					cout << "Invalid Option!";
				}
			}
			ptr_admin->~Admin();
		}
		else if (user_input == 0){
			cout << "Have a nice day!";
			continue;
		}
		else {
			cout << "Invalid Option!" << endl;
		}

	}
	
	return 0;
}