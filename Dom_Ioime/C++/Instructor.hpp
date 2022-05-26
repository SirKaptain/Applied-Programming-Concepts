#pragma once
#include "User.hpp"
class Instructor :
    public User
{

public:
    //constructor
    Instructor();
    Instructor(string first_name, string last_name, string id);

    //Destructor
    ~Instructor();

    //methods
    void print_schedule();
    void print_classlist();
    void search_course();
};

