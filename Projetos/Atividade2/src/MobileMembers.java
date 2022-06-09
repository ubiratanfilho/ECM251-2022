public class MobileMembers extends Membro{
    // Contrutor
    public MobileMembers(String usuario, String email) {
        super(usuario, email);
    }

    // posta uma mensagem diferente caso o horário seja regular e outra
    // caso extra
    @Override
    public void postarMensagem() {
        if (Sistema.getHorario() == enumHorario.REGULAR){
            System.out.println("Happy Coding!\n");
        }
        else{
            System.out.println("Happy_C0d1ng. Maskers\n");
        }
    }
    
}
