// Ubiratan da Motta Filho R.A 20.00928-3

public class Sistema {
    public void run() {
        // Cria usuário e veículos
        Usuario usuario = new Usuario("Ubiratan");
        Carro carro = new Carro(20, "Carro");
        Moto moto = new Moto(30, "Moto");
        Patinete patinete = new Patinete(40, "Patinete");
        Bicicleta bicicleta = new Bicicleta(50, "Bicicleta");
        
        // Exibe usuário e veículos
        System.out.println("Usuário e veículos");
        System.out.println(usuario);
        System.out.println(carro);
        System.out.println(moto);
        System.out.println(patinete);
        System.out.println(bicicleta);

        // Troca veículos e testa
        System.out.println("\nTrocando veículo do usuário e exibindo eles");
        usuario.trocarBem(carro);
        usuario.trocarBem(moto);
        usuario.trocarBem(patinete);
        usuario.trocarBem(bicicleta);
    }
}
