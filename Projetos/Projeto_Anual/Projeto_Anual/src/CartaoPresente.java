public class CartaoPresente {
    private String codigo; // codigo do cartao presente
    private String tipo; // tipo do cartao presente (jogo ou créditos)
    private Double valor; // valor do cartao presente (se for jogo, será o valor do jogo)
    private String descricao; // descricao do cartao presente
    private String validade; // data de validade do cartao presente
    private String titulo; // titulo do cartao presente

    // Construtor
    public CartaoPresente(String codigo, String tipo, Double valor, String descricao, String validade, String titulo) {
        this.codigo = codigo;
        this.tipo = tipo;
        this.valor = valor;
        this.descricao = descricao;
        this.validade = validade;
        this.titulo = titulo;
    }
}
