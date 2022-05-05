import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        //Usuario escolhe a jogada
        Jogada jogada1 = new Spock();
        //Sorteio da jogada para o PC
        Jogada jogada2 = sortearJogada();
        //Avaliação das jogadas
        String resultado = avaliaJogadas(jogada1, jogada2);
        //Exibição do resultado
        System.out.println("Jogada 1: " + jogada1);
        System.out.println("Jogada 2: " + jogada2);
        System.out.println("Resultado:" + resultado);
    }

    private static Jogada sortearJogada() {
        Jogada jogadas[] = {new Pedra(), new Papel(), new Tesoura(), new Lagarto(), new Spock()};
        return jogadas[ThreadLocalRandom.current().nextInt(0, 5)];
    }

    private static String avaliaJogadas(Jogada jogada1, Jogada jogada2) {
        if(jogada1.verificarVenceu(jogada2))
            return "Jogada 1";
        if(jogada2.verificarVenceu(jogada1))
            return "Jogada 2";
        return "Empate";
    }
}