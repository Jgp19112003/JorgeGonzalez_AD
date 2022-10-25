import java.io.BufferedReader;
import java.io. IOException;
import java.io.InputStreamReader;

public class Hijo{

    public static void main(String[] args) {

        String leer;
        int contador = 0;


        try {

// BufferedReader para recibir datos del padre

            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            leer = br.readLine();

            for(int i = 0;i < leer.length();i++) {
                if ((leer.charAt(i)=='a') || (leer.charAt(i)=='e') || (leer.charAt(i)=='i') || (leer.charAt(i)=='o') || (leer.charAt(i)=='u')){
                    contador++;
                }
            }

            System.out.println("Frase en mayuscula: " + leer.toUpperCase() +  "  Tiene: " + contador + " vocales" + "  Tiene: " + leer.length() + " letras");



        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
