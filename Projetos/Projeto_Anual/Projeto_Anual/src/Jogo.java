public class Jogo {
    private String nome; // Nome do jogo
    private String[] plataformas; // Plataformas que o jogo está disponível
    private String[] trofeus; // Trofeus que o jogo possui
    private Double preco; // Preço do jogo
    private Double avaliacao=0.0; // Avaliação do jogo
    private Perfil[] jogadores={}; // Jogadores que jogaram o jogo

    // Construtor
    public Jogo(String nome, String[] plataformas, String[] trofeus, Double preco) {
        this.nome = nome;
        this.plataformas = plataformas;
        this.trofeus = trofeus;
        this.preco = preco;
    }
}
