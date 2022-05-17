#pragma once
#include "User.h"
class Student :
    public User
{

public:
    //constructor
    Student();
    Student(string first_name, string last_name, string id);

    //Destructor
    ~Student();

    //methods
    void search_course();
    void add_course();
    void drop_course();
    void print_schedule();
};

