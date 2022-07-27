from Student import Student
from Instructor import Instructor
from Admin import Admin

outp = open('Lab_6_Output.txt', 'w')
student = Student("Dom", "Ioime", "W00397674")
instructor = Instructor("Ahmed", "Hassebo", "W00111111")
admin = Admin("Mark", "Thompson", "W00999999")
#student
def testcase_student():
    s = open('Lab_6_Student.txt', 'r')
    inst = 1
    line = s.readline()
    #print(line)
    pass_fail = "N/A"
    student_id = student.id
    student_pw = "1234"
    student_search = student.search_course()
    #print(student_id)
    if student_id != line:
        pass_fail = str("Student test 1 pass\n")
    else:
        pass_fail = str("Student test 1 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student_id == line:
        pass_fail = str("Student test 2 pass\n")
    else:
        pass_fail = str("Student test 2 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student_pw != line:
        pass_fail = str("Student test 3 pass\n")
    else:
        pass_fail = str("Student test 3 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student_search == line:
        pass_fail = str("Student test 4 pass\n")
    else:
        pass_fail = str("Student test 4 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student_search != line:
        pass_fail = str("Student test 5 pass\n")
    else:
        pass_fail = str("Student test 5 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    s.close()

#instructor
def testcase_instructor():
    i = open('Lab_6_Instructor.txt', 'r')
    inst = 1
    line = i.readline()
    print(line)
    pass_fail = "N/A"
    instructor_id = instructor.id
    instructor_pw = "1234"
    instructor_search = instructor.search_course()

    if instructor_id != line:
        pass_fail = str("Instructor test 1 pass\n")
    else:
        pass_fail = str("Instructor test 1 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor_id == line:
        pass_fail = str("Instructor test 2 pass\n")
    else:
        pass_fail = str("Instructor test 2 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor_pw != line:
        pass_fail = str("Instructor test 3 pass\n")
    else:
        pass_fail = str("Instructor test 3 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor_pw == line:
        pass_fail = str("Instructor test 4 pass\n")
    else:
        pass_fail = str("Instructor test 4 fail")
    outp.write(pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor_search != line:
        pass_fail = str("Instructor test 5 pass\n")
    else:
        pass_fail = str("Instructor test 5 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    courselist = ""
    ci = open('Course_list.txt', 'r')
    line = ci.readline()
    courselist = courselist+" "+line
    line = ci.readline()
    courselist = courselist+" "+line
    line = ci.readline()
    courselist = courselist+" "+line
    line = ci.readline()
    courselist = courselist+" "+line
    line = ci.readline()
    courselist = courselist+" "+line
    print(courselist)
    ci.close()
    outp.write(courselist)
    i.close()

#admin
def testcase_admin():
    a = open('Lab_6_Admin.txt', 'r')
    line = a.readline()
    print(line)
    inst = 1
    pass_fail = "N/A"
    admin_id = admin.id
    admin_pw = "1234"
    admin_search = admin.search_course()
    if admin_id != line:
        pass_fail = str("Admin test 1 pass\n")
    else:
        pass_fail = str("Student test 1 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_id == line:
        pass_fail = str("Admin test 2 pass\n")
    else:
        pass_fail = str("Student test 2 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_pw != line:
        pass_fail = str("Admin test 3 pass\n")
    else:
        pass_fail = str("Admin test 3 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_pw == line:
        pass_fail = str("Admin test 4 pass\n")
    else:
        pass_fail = str("Admin test 4 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_search != line:
        pass_fail = str("Admin test 5 pass\n")
    else:
        pass_fail = str("Admin test 5 fail\n")
    outp.write(pass_fail)
    inst = inst + 1
    add_remove()
    add_remove()
    a.close()


def add_remove():
    num = ""
    count = 0
    a = open('Lab_6_Instructor.txt', 'r')
    ar = open('courses_lab_6', 'r')
    arw = open('new_courses.txt', 'w')
    lines = []
    lines = ar.readlines()
    for line in ar:
        if line.strip():
            count += 1
    choice = a.readline()
    if choice == 1:
        add = a.readline()
        add = str(add)
        flag = 0
        index = 0
        for line in ar:
            index +=1
            if add in line:
                flag = 1
        if flag == 1:
            print("That course is already in the schedule")
        else:
            course = a.readline()
            department = a.readline()
            start_time = a.readline()
            end_time = a.readline()
            semester = a.readline()
            year = a.readline()
            credits = a.readline()
            oldcourses = ar.read()
            arw.write(oldcourses)
            wholeline = add+ " " + course +" "+department+" "+start_time+" "+end_time+" "+semester+" "+year+" "+credits
            print(wholeline)
            arw.write(wholeline)
    elif choice == 2:
        flag = 0
        index = 0
        remove = a.readline()
        remove = str(remove)
        for line in ar:
            index +=1
            if remove in line:
                flag = 1
                break
        if flag == 0:
            print("CRN not found")
        else:
            for number, line in enumerate(lines):
                if number not in [index]:
                    arw.write(line)
                
    else:
        print("Invalid input")
    
    arw.close
    ar.close
        
    

def main():
    test = 100
    while (test!= 0):
        test = input("Which test would you like to run? (1 - Student, 2 - Instructor, 3 - Admin, 0 - Exit\n")
        test = int(test)
        if test == 1:
            testcase_student()
            
        elif test == 2:
            testcase_instructor()
            
        elif test == 3:
            testcase_admin()
            
        else:
            print("Choose a valid option\n")
            

main()