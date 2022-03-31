import java.time.LocalDate;
import java.time.Period;

public class Sistema {
    public void run(){
        Cliente cliente = new Cliente("Endevour", "456789", "putzsousegundo@gmail.com");
        Conta conta = new Conta(9865,
        cliente);
        System.out.println(conta);

        Titulo titulo = new Titulo(100, 5, LocalDate.of(2022, 3, 30));
    }

    public boolean pagarTitulo(Titulo titulo, Conta conta){
        LocalDate prazo = titulo.getData();
        LocalDate hoje = LocalDate.now();
        double valor;
        
        if(prazo.compareTo(hoje) <= 0){
            valor = titulo.getValor();
        }
        else{
            int dias_atraso = Period.between(prazo, hoje).getDays()
            valor = titulo.getValor() + titulo.getValor() * titulo.getMultaDiaria() / 100 * dias_atraso;
        }
        
        if (conta.sacar(valor)){
            System.out.println("Titulo pago com sucesso!");
        }
        else{
            System.out.println("Não foi possível pagar o titulo!");
        }
        return true;
}