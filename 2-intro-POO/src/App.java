public class App {
    public static void main(String[] args) throws Exception {
        // Instanciando a classe Caneta
        Caneta caneta = new Caneta();
        // Atribuindo valores aos atributos da classe Caneta
        caneta.modelo = "Bic";
        caneta.cor = "Azul";
        caneta.ponta = 0.5;
        caneta.carga = 50;
        // Chamando o método escrever da classe Caneta
        caneta.escrever("Hello World!");
    }
}