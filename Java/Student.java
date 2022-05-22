public class Student extends User{
    Student(){
        super();
    }

    Student(String first_name, String last_name, String id){
        super(first_name, last_name, id);
    }

    public void search_course(){
        System.out.println("Search Course for Student!");
    }
    public void add_course(){
        System.out.println("Add Course for Student!");
    }
    public void drop_course(){
        System.out.println("Drop Course for Student!");
    }
    public void print_schedule(){
        System.out.println("Print Schedule for Student!");
    }

}
