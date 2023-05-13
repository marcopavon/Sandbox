import java.util.ArrayList;


public class First {
  Integer x;
  double floatNumber;
  String type;
  boolean active;

  // Create a class constructor for the Main class - Type and variable needs to be declarated above
  public First() {
    x = 5;
    floatNumber = 5.7; 
    type = "Sample";
    active = true;
  }
  // Method
  static void myMethod() {
    Integer x = 8;
    String owner = "napoleon";
    System.out.println("Hello World! "+x +owner);
  }

  //method with Array
  static void myArray() {
    ArrayList<String> cars = new ArrayList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
  }
  

  public static void main(String[] args) {
    myMethod();
    myArray();
    First objekt = new First();
    System.out.println(objekt.x);
  }
}
