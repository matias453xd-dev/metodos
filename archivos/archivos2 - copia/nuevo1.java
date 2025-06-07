public class Matias {
    public static void main(String args[]) {
        System.out.println("Hola mundo");

        String myString = "Esto es una cadena de texto";
        myString = "Aquí cambio el valor de la cadena de texto";
        System.out.println(myString);

        int myInt = 7;
        myInt = myInt + 5;
        System.out.println(myInt);
        System.out.println(myInt + 1);

        Double myDouble = 6.5;
        System.out.println(myDouble);

        float myFloat = 6.5f; // Cambiado a float y agregado el sufijo 'f'
        System.out.println(myFloat);
        System.out.println(myFloat + myDouble);
        System.out.println(myFloat + myDouble + myInt); // Suma de los tres numeros

        boolean myBoolean = true; // Cambiado a minúsculas
        myBoolean = false;
        System.out.println(myBoolean);

        // Comprobación de nulidad eliminada, ya que myFloat no puede ser null
    }
}