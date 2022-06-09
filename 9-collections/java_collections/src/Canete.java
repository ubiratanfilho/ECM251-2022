public class Canete {
    public final String cor;
    public final double ponta;
    
    public Canete(String cor, double ponta) {
        this.cor = cor;
        this.ponta = ponta;
    }

    @Override
    public String toString() {
        return "Canete [cor=" + cor + ", ponta=" + ponta + "]";
    }
}
