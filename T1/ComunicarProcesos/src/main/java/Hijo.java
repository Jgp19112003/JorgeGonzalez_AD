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

            HiloProceso hilo1 = new HiloProceso(contador,leer.length());


            hilo1.start();


            try {
                hilo1.join();


                double r1 = hilo1.getResultado();


                double media = (double) contador / leer.length();

                System.out.println("Media: " + media);

            } catch (InterruptedException ex) {
                System.out.println(ex.getMessage());
            }

        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
