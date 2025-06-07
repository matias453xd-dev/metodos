public class Operadores {
  public static void main(String[] args) {
    int x = 5, y;
    y = x++; // Incremento postfijo: y = 5, luego x = 6
    System.out.println(y); // Imprime 5 y luego realiza la suma
    System.out.println(x); // x suma 1 e imprime
    
    y = ++x; // Incremento prefijo: x = 7, luego y = 7
    System.out.println(y); // Imprime 7
    System.out.println(x); 
    
    float z = 13.6f;
    int IntRound = Math.round(z);
    System.out.println("El numero, "+ z + " redondeado es, " + IntRound);
    }
}