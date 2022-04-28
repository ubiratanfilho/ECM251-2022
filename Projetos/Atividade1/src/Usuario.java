// Ubiratan da Motta Filho R.A 20.00928-3

public class Usuario {
    // Atributos
    private String nome;
    private Veiculo veiculo;

    // Construtor
    public Usuario(String nome) {
        this.nome = nome;
    }

    // Testa se o veículo do usuário foi mesmo trocado
    public void testar(){
        System.out.println("ID do veículo: " + veiculo.getId());
        System.out.println("Custo: R$" + veiculo.getCustoHora() + " por hora");
    }

    // Troca o veículo do usuário
    public void trocarBem(Veiculo novo){
        this.veiculo = novo;
        testar();
    }

    @Override
    public String toString() {
        return "Usuario [nome=" + nome + ", veiculo=" + veiculo + "]";
    }
}
