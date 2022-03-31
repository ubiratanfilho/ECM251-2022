// Ubiratan da Motta Filho R.A 20.00928-3

public class Transacoes {
    // Gera um requerimento de saque (nosso QRCode)
    public String gerarRequerimento(Conta pedinte, double valor){
        return pedinte.getIdConta() + ";" 
        + pedinte.getUsuario().getNome().toUpperCase()
        + ";" + valor;
    }

    // Realiza uma transação
    public boolean realizarTransacao(Conta pagador, Conta recebedor, String qrcode){
        String dados[] = qrcode.split(";");
        int idConta = Integer.parseInt(dados[0]);
        String nome = dados[1];
        double valor = Double.parseDouble(dados[2]);

        if(recebedor.getIdConta() == idConta && recebedor.getUsuario().getNome().toUpperCase().equals(nome) && pagador.sacar(valor)){
            recebedor.depositar(valor);
            return true;
        }
        return false;
    }
}
