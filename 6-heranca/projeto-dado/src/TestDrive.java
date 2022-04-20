public class TestDrive{
    public static void executar(){
        Dado d1 = new Dado("1234");
        System.out.println("Dado criado");
        System.out.println("Face atual: " + d1.faceAtual());
        // Sorteia nova face
        d1.rodar();
        System.out.println("Face atual: " + d1.faceAtual());

        Dado d2 = new DadoD6("2222");
    }
}