// Ubiratan da Motta Filho R.A 20.00928-3

import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {
    // Atributos
    private int id;
    private float custo_hora;
    private String tipo;

    // Construtor
    public Veiculo(float custo_hora, String tipo) {
        this.id = ThreadLocalRandom.current().nextInt(10000, 100000);
        this.custo_hora = custo_hora;
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "Veiculo [custo_hora=" + custo_hora + ", id=" + id + ", tipo=" + tipo + "]";
    }

    // Getters e Setters
    public int getId() {
        return id;
    }

    public float getCustoHora() {
        return custo_hora;
    }
}

