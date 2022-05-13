public class Perfil{
    private String[] trofeus={}; // Trofeus que o perfil possui
    private Jogo[] jogos={}; // jogos que o perfil já jogou
    private EnumPlataforma[] plataformas={}; // plataformas que o perfil utiliza
    private String nome;

    // Construtor
    public Perfil(String nome) {
        this.nome = nome;
    }
    
}
