import java.util.Scanner;

public class ArreglosJava {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        // Inicializacion del arreglo de nombres
        String[] nombres = new String[3];
        nombres[0] = "lol";
        nombres[1] = "xd";
        nombres[2] = "yepa";
        
        // Imprimir los nombres
        for (String nombre : nombres) {
            System.out.println(nombre);
        }
        
        // Inicializacion del arreglo de notas
        float[] notas = new float[3];
        
        // Leer las notas del usuario
        System.out.println("Ingrese 3 notas:");
        for (int i = 0; i < notas.length; i++) {
            notas[i] = input.nextFloat();
        }
        
        // Imprimir las notas
        System.out.println("Las notas ingresadas son:");
        for (float nota : notas) {
            System.out.println(nota);
        }
    }
}
