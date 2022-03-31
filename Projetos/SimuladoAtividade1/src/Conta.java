// Ubiratan da Motta Filho R.A 20.00928-3

public class Conta {
    //Atributos
    private int idConta;
    private double saldo;
    private Usuarios usuario;
    private static int contador = 0;

    //Construtor
    public Conta(double saldo, Usuarios usuario) {
        this.saldo = saldo;
        this.usuario = usuario;
        this.idConta = ++contador;
    }

    //Métodos
    //Getters e Setters
    public int getIdConta() {
        return idConta;
    }
    public double getSaldo() {
        return saldo;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    public Usuarios getUsuario() {
        return usuario;
    }

    // Visualizar informações da conta
    public void visualizarInfo() {
        System.out.println("Usurário: " + this.usuario.getNome() + "Saldo: " + this.saldo);
    }

    // Sacar e depositar
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    
}