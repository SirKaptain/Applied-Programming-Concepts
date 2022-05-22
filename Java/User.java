import java.util.Scanner;

public class User {

    String first_name;
    String last_name;
    String id;

    public User(){
        first_name = "First Name";
        last_name = "Last Name";
		id = "W00000000";
    }
        
    public User(String first_name, String last_name, String id){
        this.first_name = first_name;
        this.last_name = last_name;
        this.id = id;
    }

    public void set_first_name(String new_first_name){
        first_name = new_first_name;
    }

    public void set_last_name(String new_last_name){
        last_name = new_last_name;
    }

    public void set_id(String new_id){
        id = new_id;
    }

    public void show_info(){
        System.out.println(first_name);
        System.out.println(last_name);
        System.out.println(id);
    }

    public void edit_info(){
        Scanner reader = new Scanner(System.in);
        while (true){
            System.out.println("What information would you like to edit?:");
            System.out.println("First Name(1)   Last Name(2)");
            System.out.println("ID(3)           Back(0)");
            System.out.println("Input: ");
            int user_input = reader.nextInt();
            if (user_input == 1){
                System.out.println("What would you like to change your first name to?");
                System.out.println("New First Name: ");
                String new_info = reader.next();
                first_name = new_info;
            }
            else if (user_input == 2){
                System.out.println("What would you like to change your Last name to?");
                System.out.println("New Last Name: ");
                String new_info = reader.next();
                last_name = new_info;
            }
            else if (user_input == 3){
                System.out.println("What would you like to change your id to?");
                System.out.println("New ID: ");
                String new_info = reader.next();
                id = new_info;
            }
            else if (user_input == 0){
                break;
            }
            else{
                System.out.println("Invalid Option!");
            }
        }
    }
}


