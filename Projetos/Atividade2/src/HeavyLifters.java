public class HeavyLifters extends Membro{
    // Contrutor
    public HeavyLifters(String usuario, String email) {
        super(usuario, email);
    }

    // posta uma mensagem diferente caso o horário seja regular e outra
    // caso extra
    @Override
    public void postarMensagem() {
        if (Sistema.getHorario() == enumHorario.REGULAR){
            System.out.println("Podem contar conosco!\n");
        }
        else{
            System.out.println("N00b_qu3_n_Se_r3pita.bat\n");
        }
    }
    
}
