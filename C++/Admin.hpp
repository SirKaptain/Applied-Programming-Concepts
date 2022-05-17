#pragma once
#include "User.h"
class Admin :
    public User
{

public:
    //constructor
    Admin();
    Admin(string first_name, string last_name, string id);

    //Destructor
    ~Admin();

    //methods
    void add_course();
    void remove_course();
    void add_user();
    void remove_user();
    void add_student_to_course();
    void remove_student_from_course();
    void search_roster();
    void print_roster();
    void search_course();
    void print_course();
};

