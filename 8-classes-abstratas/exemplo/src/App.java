public class App {
    public static void main(String[] args) throws Exception {
        Configuracao c1;
        Configuracao c2;

        c1 = new ConfiguracaoDesenvolvimento("localhost", "localhost:5000");
        c2 = new ConfiguracaoProducao("localhost", "localhost:5000", "admin");

        System.out.println("Conf1: " + c1);
        System.out.println("Conf2: " + c2);
    }
}
