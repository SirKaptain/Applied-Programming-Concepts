public class Admin extends User{
    Admin(){
        super();
    }
    Admin(String first_name, String last_name, String id){
        super(first_name, last_name, id);
    }

    public void add_course(){
        System.out.println("Add Course for Admin!");
    }
    public void remove_course(){
        System.out.println("Remove Course for Admin!");
    }
    public void add_user(){
        System.out.println("Add User for Admin!");
    }
    public void remove_user(){
        System.out.println("Remove User for Admin!");
    }
    public void add_student_to_course(){
        System.out.println("Add Student to Course for Admin!");
    }
    public void remove_student_from_course(){
        System.out.println("Remove Student from Course for Admin!");
    }
    public void search_roster(){
        System.out.println("Search Roster for Admin!");
    }
    public void print_roster(){
        System.out.println("Print Roster for Admin!");
    }
    public void search_course(){
        System.out.println("Search Course for Admin!");
    }
    public void print_course(){
        System.out.println("Print Course for Admin!");
    }
}
