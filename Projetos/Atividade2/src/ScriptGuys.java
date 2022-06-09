public class ScriptGuys extends Membro{
    // Contrutor
    public ScriptGuys(String usuario, String email) {
        super(usuario, email);
    }

    // posta uma mensagem diferente caso o horário seja regular e outra
    // caso extra
    @Override
    public void postarMensagem() {
        if (Sistema.getHorario() == enumHorario.REGULAR){
            System.out.println("Prazer em ajudar novos amigos de código!\n");
        }
        else{
            System.out.println("QU3Ro_S3us_r3curs0s.py\n");
        }
    }
    
}