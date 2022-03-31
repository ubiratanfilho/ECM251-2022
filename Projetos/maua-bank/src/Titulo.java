import java.time.LocalDate;

public class Titulo {
    private double valor;
    private double multaDiaria;
    private LocalDate data;
    
    public Titulo(double valor, double multaDiaria, LocalDate data){
        this.setValor(valor);
        this.setMultaDiaria(multaDiaria);
        this.setData(data);
    }

    public LocalDate getData() {
        return data;
    }

    private void setData(LocalDate data) {
        this.data = data;
    }

    public double getMultaDiaria() {
        return multaDiaria;
    }

    private void setMultaDiaria(double multaDiaria) {
        this.multaDiaria = multaDiaria;
    }

    public double getValor() {
        return valor;
    }

    private void setValor(double valor) {
        this.valor = valor;
    }
}
