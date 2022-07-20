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
    print(line)
    pass_fail = "N/A"
    student_id = student.id
    student_pw = "1234"
    student_search = student.search_course()
    print(student_id)
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
    line = i.readline()
    print(line)
    pass_fail = "N/A"
    instructor_id = instructor.id
    instructor_pw = "1234"
    if instructor.id() != line:
        pass_fail = str("Instructor test 1 pass")
    else:
        pass_fail = str("Instructor test 1 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.id() != line:
        pass_fail = str("Instructor test 2 pass")
    else:
        pass_fail = str("Instructor test 2 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.password() != line:
        pass_fail = str("Instructor test 3 pass")
    else:
        pass_fail = str("Instructor test 3 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.password() != line:
        pass_fail = str("Instructor test 4 pass")
    else:
        pass_fail = str("Instructor test 4 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.search_course() != line:
        pass_fail = str("Instructor test 5 pass")
    else:
        pass_fail = str("Instructor test 5 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    i.close()

#admin
def testcase_admin():
    a = open('Lab_6_Admin.txt', 'r')
    line = a.readline()
    print(line)
    pass_fail = "N/A"
    admin_id = admin.id
    admin_pw = "1234"
    if admin.id() != line:
        pass_fail = str("Admin test 1 pass")
    else:
        pass_fail = str("Student test 1 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_id != line:
        pass_fail = str("Admin test 2 pass")
    else:
        pass_fail = str("Student test 2 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_pw != line:
        pass_fail = str("Admin test 3 pass")
    else:
        pass_fail = str("Admin test 3 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin_pw != line:
        pass_fail = str("Admin test 4 pass")
    else:
        pass_fail = str("Admin test 4 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin.search_course() != line:
        pass_fail = str("Admin test 5 pass")
    else:
        pass_fail = str("Admin test 5 fail")
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    a.close()

testcase_student()
#testcase_instructor()
#testcase_admin()