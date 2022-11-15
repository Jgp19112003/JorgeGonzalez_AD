public class HiloProceso extends Thread {

    private int vocales;
    private int longuitud;
    private int resultado;


    public HiloProceso(int vocales, int longuitud) {
        this.vocales = vocales;
        this.longuitud = longuitud;
    }

    @Override
    public void run() {

        this.resultado = vocales / longuitud;

    }

    public double getResultado() {
        return resultado;
    }

}
