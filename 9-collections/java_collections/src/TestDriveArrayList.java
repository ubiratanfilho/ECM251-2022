import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args) {
        ArrayList canetas = new ArrayList<Canete>();

        canetas.add(new Canete("Azul", 0.5));
        canetas.add(new Canete("Verde", 0.7));
        canetas.add(new Canete("Vermelha", 1.0));
    }
    
}
