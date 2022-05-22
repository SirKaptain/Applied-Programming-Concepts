import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int user_input = 1;
        System.out.println("Welcome to Leopard Web!");
        while (user_input != 0){
            System.out.println("Choose an option:");
            System.out.println("Student(1)		Instructor(2)");
            System.out.println("Admin(3)		Exit(0)");
            System.out.println("Input: ");
            user_input = reader.nextInt();

            if (user_input == 1){
                Student student = new Student("Dom", "Ioime", "W00397674");
                while (user_input != 0){
                    System.out.println("Choose an option:");
                    System.out.println("Add Course(1)			Drop Course(2)");
                    System.out.println("Print Schedule(3)		Search Course(4)");
                    System.out.println("Show Info(5)			    Edit Info(6)");
                    System.out.println("Exit(0)");
                    System.out.println("Input: ");
                    user_input = reader.nextInt();
                    if (user_input == 1){
                        student.add_course();
                    }
                    else if (user_input == 2){
                        student.drop_course();
                    }
                    else if (user_input == 3){
                        student.print_schedule();
                    }
                    else if (user_input == 4){
                        student.search_course();
                    }
                    else if (user_input == 5){
                        student.show_info();
                    }
                    else if (user_input == 6){
                        student.edit_info();
                    }
                    else if (user_input == 0){
                        continue;
                    }
                    else{
                        System.out.println("Invalid Option!");
                    }
                }
            }
            else if (user_input == 2){
                Instructor instructor = new Instructor("Ahmed", "Hassebo", "W00111111");
                while (user_input != 0){
                    System.out.println("Choose an option:");
                    System.out.println("Print Schedule(1)		Print Classlist(2)");
                    System.out.println("Search Course(3)		Show Info(4)");
                    System.out.println("Edit Info(5)			Exit(0)");
                    System.out.println("Input: ");
                    user_input = reader.nextInt();
                    if (user_input == 1){
                        instructor.print_schedule();
                    }
                    else if (user_input == 2){
                        instructor.print_classlist();
                    }
                    else if (user_input == 3){
                        instructor.search_course();
                    }
                    else if (user_input == 4){
                        instructor.show_info();
                    }
                    else if (user_input == 5){
                        instructor.edit_info();
                    }
                    else if (user_input == 0){
                        continue;
                    }
                    else{
                        System.out.println("Invalid Option!");
                    }
                }
            }
            else if (user_input == 3){
                Admin admin = new Admin("Mark", "Thompson", "W00999999");
                while (user_input != 0){
                    System.out.println("Choose an option:");
                    System.out.println("Add Course(1)	Remove Course(2)	Add User(3)	Remove User(4)");
                    System.out.println("Add a Student to a Course(5)	Remove a Student from a Course(6)");
                    System.out.println("Search Roster(7)	Print Roster(8)		Search Course(9)	Print Course(10)");
                    System.out.println("Show Info(11)	Edit Info(12)	Exit(0)");
                    System.out.println("Input: ");
                    user_input = reader.nextInt();
                    if (user_input == 1){
                        admin.add_course();
                    }
                    else if (user_input == 2){
                        admin.remove_course();
                    }
                    else if (user_input == 3){
                        admin.add_user();
                    }
                    else if (user_input == 4){
                        admin.remove_user();
                    }
                    else if (user_input == 5){
                        admin.add_student_to_course();
                    }
                    else if (user_input == 6){
                        admin.remove_student_from_course();
                    }
                    else if (user_input == 7){
                        admin.search_roster();
                    }
                    else if (user_input == 8){
                        admin.print_roster();
                    }
                    else if (user_input == 9){
                        admin.search_course();
                    }
                    else if (user_input == 10){
                        admin.print_course();
                    }
                    else if (user_input == 11){
                        admin.show_info();
                    }
                    else if (user_input == 12){
                        admin.edit_info();
                    }
                    else if (user_input == 0){
                        continue;
                    }
                    else{
                        System.out.println("Invalid Option!");
                    }
                }
            }
            else if (user_input == 0){
                System.out.println("Have a nice day!");
                continue;
            }
            else {
                System.out.println("Invalid Option!");
            }
        }
        reader.close();

    }
}
