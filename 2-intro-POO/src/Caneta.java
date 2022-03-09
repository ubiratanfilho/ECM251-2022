public class Caneta {
    // Atributos da classe
    String modelo;
    String cor;
    double ponta;
    int carga;

    // Métodos da classe
    void status() {
        System.out.println("Modelo: " + this.modelo);
        System.out.println("Cor: " + this.cor);
        System.out.println("Ponta: " + this.ponta);
        System.out.println("Carga: " + this.carga);
    }
    
    void escrever(String texto) {
        System.out.println(texto);
    }
}
