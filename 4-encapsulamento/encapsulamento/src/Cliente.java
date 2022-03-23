public class Cliente {
    private String nome;
    private String cpf;
    private String email;
    private Conta conta;

    public void visualizarCliente() {
        System.out.println("Dados do cliente: ");
        System.out.println("Nome: " + this.nome);
        System.out.println("CPF: " + this.cpf);
        System.out.println("Email: " + this.email);
        System.out.println("Conta: " + this.conta);
    }

    // Construtor da classe
    public Cliente(String nome, String cpf, String email, Conta conta) {
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
        this.conta = conta;
    }

    // Métodos getters e setters
    public String getNome() {
        return this.nome;
    }
    public String getCpf() {
        return this.cpf;
    }
    public String getEmail() {
        return this.email;
    }
    public Conta getConta() {
        return this.conta;
    }   

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setEmail(String email) {
        this.email = email;
    }

}
