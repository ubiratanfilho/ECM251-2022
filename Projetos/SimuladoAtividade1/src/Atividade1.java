// Ubiratan da Motta Filho R.A 20.00928-3

public class Atividade1 {
    public void run() {
        // Cria nossos objetos
        Usuarios usuario1 = new Usuarios("UbiraTech", "ubiratec", "123");
        Usuarios usuario2 = new Usuarios("Brunao", "brunao", "123");
        Usuarios usuario3 = new Usuarios("Hugo", "hugo", "123");
        Conta conta1 = new Conta(1000000, usuario1);
        Conta conta2 = new Conta(3000, usuario2);
        Conta conta3 = new Conta(4000, usuario3);
        Transacoes transacoes = new Transacoes();

        // Visualiza as informações
        System.out.println("Antes de realizar as transações:");
        conta1.visualizarInfo();
        conta2.visualizarInfo();
        conta3.visualizarInfo();

        // Gera os QR Codes
        String qrcode1 = transacoes.gerarRequerimento(conta1, 250);
        String qrcode2 = transacoes.gerarRequerimento(conta2, 1000);
        
        // Realiza as transações
        transacoes.realizarTransacao(conta2, conta1, qrcode1);
        transacoes.realizarTransacao(conta3, conta1, qrcode1);
        transacoes.realizarTransacao(conta2, conta1, qrcode1);
        transacoes.realizarTransacao(conta3, conta2, qrcode2);

        // Visualiza as informações
        System.out.println("\nDepois de realizar as transações:");
        conta1.visualizarInfo();
        conta2.visualizarInfo();
        conta3.visualizarInfo();
    }
}
