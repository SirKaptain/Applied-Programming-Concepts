public class Instructor extends User {
    
    Instructor(){
        super();
    }
    Instructor(String first_name, String last_name, String id){
        super(first_name, last_name, id);
    }

    public void print_schedule(){
        System.out.println("Print Schedule for Instructor!");
    }
    public void print_classlist(){
        System.out.println("Print Classlist for Instructor!");
    }
    public void search_course(){
        System.out.println("Search course for Instructor!");
    }
}
