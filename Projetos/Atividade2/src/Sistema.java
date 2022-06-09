import java.util.LinkedList;

public class Sistema {
    // Atributos
    private static enumHorario horario = enumHorario.REGULAR;

    public static void run(){
        // Cria linked list vazia e adiciona usuários, um com cada função
        LinkedList<Membro> membros = new LinkedList<Membro>();
        membros.add(new BigBrothers("bira", "bira@gmail"));
        membros.add(new HeavyLifters("brunao", "brunao@gmail"));
        membros.add(new MobileMembers("igor", "igor@gmail"));
        membros.add(new ScriptGuys("cormem", "cormem@gmail"));
        
        // Exibe todos os membros e suas respectivas mensagens
        for (Membro membro : membros) {
            System.out.println(membro.getUsuario());
            membro.postarMensagem();
        }
        System.out.println("------------------------------------------------------\n");

        mudarTurno();
        // Exibe todos os membros e suas respectivas mensagens
        for (Membro membro : membros) {
            System.out.println(membro.getUsuario());
            membro.postarMensagem();
        }
        System.out.println("------------------------------------------------------\n");

        mudarTurno();
        // Remove HeavyLifters e ScriptGuys da lista
        membros.remove(1);
        membros.remove(2);
        // Exibe todos os membros e suas respectivas mensagens
        for (Membro membro : membros) {
            System.out.println(membro.getUsuario());
            membro.postarMensagem();
        }
        System.out.println("------------------------------------------------------\n");
    }

    public static enumHorario getHorario() {
        return horario;
    }

    public static void mudarTurno(){
        if (horario == enumHorario.REGULAR){
            horario = enumHorario.EXTRA;
        }
        else{
            horario = enumHorario.REGULAR;
        }
    }

}
