public class Main {
    public static String doubleChar(String s) {
        return s.replaceAll(".", "$0$0");
    }

    public static void main(String[] args) {
        System.out.println(doubleChar("The"));       // Output: TThhee
        System.out.println(doubleChar("AAbb"));      // Output: AAAAbbbb
        System.out.println(doubleChar("Hi-There"));  // Output: HHii-TThheerree
    }
}