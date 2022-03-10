public class App {
    public static void main(String[] args) throws Exception {
        // Instanciando a classe Caneta
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("Bic", "Azul", 0.5);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Bic", "Azul", 0.5);
        System.out.println("Caneta c1:\n" + c1.pegarDados());
        System.out.println("\n\nCaneta c1:" + c2.pegarDados());
        c1.escrever("\nioehfoehfiofhhfoiefheoihfoiefheiofhioefhoeifheoifheoifhoiehfoeihfoiehfeoihfeiohfoeihfeoihfoeihfeoifhoeifheoifhoeifheoihfoeihfioehfioefheiofheoifheoifhoifheoihfoifhoiehfeoihfoiehfoiehfoeihfoiehfoiehfoiehfoiehfeoihfoeihfoeihfehfoeihfoeihfoeifheoifheoifheiofhfhefhefoheofihefiohefioehfioehfoiehfoeihfeiofheiofehoehfoiehfoiehfehfehfioehfhoiefhoeihfoiehfoiehfoiehfoiefefhoefheoifhefefeofiefhefhefhefeoefheiohfefhiefhiefhiiefheoifehofeoihf!");
        c2.escrever("\nOi mundo\n!");
        System.out.println("\nCaneta c1:" + c1.pegarDados());
        System.out.println("\n\nCaneta c1:" + c2.pegarDados());
    }
}