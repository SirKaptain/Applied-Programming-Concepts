from Student import Student
from Instructor import Instructor
from Admin import Admin
outp = open('Lab_6_Output.txt', 'w')
#student
def testcase_student():
    s = open('Lab_6_Student.txt', 'r')
    inst = 1
    line = s.readline()
    print(line)
    pass_fail
    if student.username() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student.username() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student.password() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student.password() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = s.readline()
    print(line)
    if student.search_course() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    s.close()

#instructor
def testcase_instructor():
    i = open('Lab_6_Instructor.txt', 'r')
    line = i.readline()
    print(line)
    if instructor.username() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.username() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.password() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.password() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = i.readline()
    print(line)
    if instructor.search_course() != line:
        pass_fail = 1
    else:
        pass_fail = 0
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
    if admin.username() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin.username() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin.password() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin.password() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    line = a.readline()
    print(line)
    if admin.search_course() != line:
        pass_fail = 1
    else:
        pass_fail = 0
    outp.write("Test case ", inst, " - ", pass_fail)
    inst = inst + 1
    a.close()

