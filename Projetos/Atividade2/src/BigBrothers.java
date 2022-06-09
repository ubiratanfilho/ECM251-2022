public class BigBrothers extends Membro{
    // Contrutor
    public BigBrothers(String usuario, String email) {
        super(usuario, email);
    }

    // posta uma mensagem diferente caso o horário seja regular e outra
    // caso extra
    @Override
    public void postarMensagem() {
        if (Sistema.getHorario() == enumHorario.REGULAR){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!!\n");
        }
        else{
            System.out.println("...\n");
        }
    }
    
}
