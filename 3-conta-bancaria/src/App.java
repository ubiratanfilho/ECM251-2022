public class App {
    public static void main(String[] args) throws Exception {
        // declara um objeto tipo Conta
        Conta minhaConta = new Conta();
        Conta outraConta = new Conta();

        minhaConta.saldo = 1000;
        minhaConta.numero = 123;
        outraConta.saldo = 2000;
        outraConta.numero = 456;

        minhaConta.visualizarSaldo();
        outraConta.visualizarSaldo();

        minhaConta.transferirDinheiro(100, outraConta);
        minhaConta.visualizarSaldo();
        outraConta.visualizarSaldo();
    }
}
