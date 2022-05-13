import java.util.Arrays;

public class Conta {
    // Atributos
    // informações básicas da conta
    private String nome;
    private String sobrenome;
    private String nome_usuario;
    private String email;
    private String CPF;
    private String data_nascimento;
    private String telefone;
    private String[] redes_sociais={};

    // informações de compras
    private int pontosPromocionais=0; // Pontos promocionais da conta
    private Transacao[] transacoes={}; // transacoes que a conta realizou
    private Jogo[] wishlist={}; // wishlist da conta
    private Jogo[] carrinho={}; // carrinho da conta
    private EnumMetodoPagamento[] MetodoPagamento={}; // Metodos de pagamento que a conta utiliza
    private Double saldo=0.0; // saldo da conta

    // informações de jogos
    private Perfil[] perfis={}; // Perfis dentro da conta
    private Jogo[] jogos={}; // jogos que a conta possui
    private EnumPlataforma[] plataformas={}; // plataformas que a conta utiliza
    private Feedback[] feedbacks={}; // feedbacks que a conta escreveu

    // Construtor
    public Conta(String nome, String sobrenome, String nome_usuario, String email,
            String CPF, String data_nascimento,
            String telefone) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.email = email;
        this.CPF = CPF;
        this.data_nascimento = data_nascimento;
        this.telefone = telefone;
        this.nome_usuario = nome_usuario;
    }

    // Métodos
    @Override
    public String toString() {
        return "Usuário: " + nome_usuario + "\n" +
                "Nome: " + nome + " " + sobrenome + "\n" +
                "Email: " + email + "\n" +
                "CPF: " + CPF + "\n" +
                "Data de nascimento: " + data_nascimento + "\n" +
                "Telefone: " + telefone + "\n" +
                "Redes sociais: " + Arrays.toString(redes_sociais) + "\n" +
                "Pontos promocionais: " + pontosPromocionais + "\n" +
                "Transações: " + Arrays.toString(transacoes) + "\n" +
                "Wishlist: " + Arrays.toString(wishlist) + "\n" +
                "Carrinho: " + Arrays.toString(carrinho) + "\n" +
                "Metodos de pagamento: " + Arrays.toString(MetodoPagamento) + "\n" +
                "Saldo: " + saldo + "\n" +
                "Perfis: " + Arrays.toString(perfis) + "\n" +
                "Jogos: " + Arrays.toString(jogos) + "\n" +
                "Plataformas: " + Arrays.toString(plataformas) + "\n" +
                "Feedbacks: " + Arrays.toString(feedbacks);    
    }

    // Getters e Setters
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }
    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public String getNome_usuario() {
        return nome_usuario;
    }
    public void setNome_usuario(String nome_usuario) {
        this.nome_usuario = nome_usuario;
    }

    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }

    public String getCPF() {
        return CPF;
    }
    public void setCPF(String cPF) {
        CPF = cPF;
    }

    public String getData_nascimento() {
        return data_nascimento;
    }
    public void setData_nascimento(String data_nascimento) {
        this.data_nascimento = data_nascimento;
    }

    public String getTelefone() {
        return telefone;
    }
    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String[] getRedes_sociais() {
        return redes_sociais;
    }

    public int getPontosPromocionais() {
        return pontosPromocionais;
    }
    public void setPontosPromocionais(int pontosPromocionais) {
        this.pontosPromocionais = pontosPromocionais;
    }

    public Transacao[] getTransacoes() {
        return transacoes;
    }

    public Jogo[] getWishlist() {
        return wishlist;
    }

    public Jogo[] getCarrinho() {
        return carrinho;
    }

    public EnumMetodoPagamento[] getMetodoPagamento() {
        return MetodoPagamento;
    }

    public Double getSaldo() {
        return saldo;
    }
    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

    public Perfil[] getPerfis() {
        return perfis;
    }

    public Jogo[] getJogos() {
        return jogos;
    }

    public EnumPlataforma[] getPlataformas() {
        return plataformas;
    }

    public Feedback[] getFeedbacks() {
        return feedbacks;
    }
    // Adders
    public void addRedeSocial(String rede_social) {
        String[] aux = new String[redes_sociais.length + 1];
        for (int i = 0; i < redes_sociais.length; i++) {
            aux[i] = redes_sociais[i];
        }
        aux[aux.length - 1] = rede_social;
        redes_sociais = aux;
    }
    public void addTransacao(Transacao transacao) {
        Transacao[] aux = new Transacao[transacoes.length + 1];
        for (int i = 0; i < transacoes.length; i++) {
            aux[i] = transacoes[i];
        }
        aux[aux.length - 1] = transacao;
        transacoes = aux;
    }
    public void addWishlist(Jogo jogo) {
        Jogo[] aux = new Jogo[wishlist.length + 1];
        for (int i = 0; i < wishlist.length; i++) {
            aux[i] = wishlist[i];
        }
        aux[aux.length - 1] = jogo;
        wishlist = aux;
    }
    public void addCarrinho(Jogo jogo) {
        Jogo[] aux = new Jogo[carrinho.length + 1];
        for (int i = 0; i < carrinho.length; i++) {
            aux[i] = carrinho[i];
        }
        aux[aux.length - 1] = jogo;
        carrinho = aux;
    }
    public void addMetodoPagamento(EnumMetodoPagamento metodoPagamento) {
        EnumMetodoPagamento[] aux = new EnumMetodoPagamento[MetodoPagamento.length + 1];
        for (int i = 0; i < MetodoPagamento.length; i++) {
            aux[i] = MetodoPagamento[i];
        }
        aux[aux.length - 1] = metodoPagamento;
        MetodoPagamento = aux;
    }
    public void addPerfil(Perfil perfil) {
        Perfil[] aux = new Perfil[perfis.length + 1];
        for (int i = 0; i < perfis.length; i++) {
            aux[i] = perfis[i];
        }
        aux[aux.length - 1] = perfil;
        perfis = aux;
    }
    public void addJogo(Jogo jogo) {
        Jogo[] aux = new Jogo[jogos.length + 1];
        for (int i = 0; i < jogos.length; i++) {
            aux[i] = jogos[i];
        }
        aux[aux.length - 1] = jogo;
        jogos = aux;
    }
    public void addPlataforma(EnumPlataforma plataforma) {
        EnumPlataforma[] aux = new EnumPlataforma[plataformas.length + 1];
        for (int i = 0; i < plataformas.length; i++) {
            aux[i] = plataformas[i];
        }
        aux[aux.length - 1] = plataforma;
        plataformas = aux;
    }
    public void addFeedback(Feedback feedback) {
        Feedback[] aux = new Feedback[feedbacks.length + 1];
        for (int i = 0; i < feedbacks.length; i++) {
            aux[i] = feedbacks[i];
        }
        aux[aux.length - 1] = feedback;
        feedbacks = aux;
    }

}
