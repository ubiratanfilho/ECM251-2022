public abstract class Membro implements PostarMensagem{
    // Atributos
    private String usuario;
    private String email;

    // Contrutor
    public Membro(String usuario, String email) {
        this.usuario = usuario;
        this.email = email;
    }

    // Getters
    public String getUsuario() {
        return usuario;
    }
}
