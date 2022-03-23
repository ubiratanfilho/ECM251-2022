public class Conta {
    // Atributos da nossa classe
    private int numero;
    private double saldo;

    // Construtor da classe
    public Conta(int numero) {
        this.numero = numero;
        this.saldo = 0;
    }

    // Métodos da nossa classe
    public void visualizarSaldo() {
        System.out.println("Saldo atual na conta " + numero + " R$: " 
        + this.saldo);
    }
    public boolean depositar(double valor) {
        if(valor < 0) return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor) {
        if(valor > this.saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!sacar(valor)) return false;
        if(!destino.depositar(valor)) return false;
        return true;
    }
} 
