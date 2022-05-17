#include <iostream>


#include "Student.h"
#include "Instructor.h"
#include "Admin.h"


using std::cin;
using std::cout;
using std::endl;


int main() {
	//Creating a student
	Student* ptr_student = new Student("Dom", "Ioime", "W00397674");

	//Testing Methods
	cout << ptr_student->show_first_name() << endl;
	cout << ptr_student->show_last_name() << endl;
	cout << ptr_student->show_id() << endl;
	ptr_student->add_course();
	ptr_student->drop_course();
	ptr_student->print_schedule();
	ptr_student->search_course();

	//Changing Name and ID
	ptr_student->set_first_name("Mod");
	ptr_student->set_last_name("Emioi");
	ptr_student->set_id("47679300W");

	//Checking for change
	cout << ptr_student->show_first_name() << endl;
	cout << ptr_student->show_last_name() << endl;
	cout << ptr_student->show_id() << endl;

	//Destruction
	ptr_student->~Student();

	//Creating Instructor
	Instructor* ptr_instructor = new Instructor("Ahmed", "Hassebo", "W00111111");

	//Testing Methods
	cout << ptr_instructor->show_first_name() << endl;
	cout << ptr_instructor->show_last_name() << endl;
	cout << ptr_instructor->show_id() << endl;
	ptr_instructor->print_classlist();
	ptr_instructor->print_schedule();
	ptr_instructor->search_course();

	//Changing Name and ID
	ptr_instructor->set_first_name("Demha");
	ptr_instructor->set_last_name("Obessah");
	ptr_instructor->set_id("11111100W");

	//Checking for change
	cout << ptr_instructor->show_first_name() << endl;
	cout << ptr_instructor->show_last_name() << endl;
	cout << ptr_instructor->show_id() << endl;

	//Destruction
	ptr_instructor->~Instructor();

	//Creating Admin
	Admin* ptr_admin = new Admin("Mark", "Thompson", "W00999999");

	//Testing Methods
	cout << ptr_admin->show_first_name() << endl;
	cout << ptr_admin->show_last_name() << endl;
	cout << ptr_admin->show_id() << endl;
	ptr_admin->add_course();
	ptr_admin->add_student_to_course();
	ptr_admin->add_user();
	ptr_admin->print_course();
	ptr_admin->print_roster();
	ptr_admin->remove_course();
	ptr_admin->remove_student_from_course();
	ptr_admin->remove_user();
	ptr_admin->search_course();
	ptr_admin->search_roster();

	//Changing Name and ID
	ptr_admin->set_first_name("KarM");
	ptr_admin->set_last_name("Nospmoht");
	ptr_admin->set_id("99999900W");

	//Checking for change
	cout << ptr_admin->show_first_name() << endl;
	cout << ptr_admin->show_last_name() << endl;
	cout << ptr_admin->show_id() << endl;

	return 0;
}