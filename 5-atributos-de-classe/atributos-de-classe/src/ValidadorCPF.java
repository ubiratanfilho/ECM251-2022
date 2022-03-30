public class ValidadorCPF {
    public static boolean validar(String cpf) {
        if (cpf.equals("11111111111") || cpf.equals("22222222222") || cpf.equals("33333333333")
                || cpf.equals("44444444444"))
            return false;

        int soma = Integer.parseInt("" + cpf.charAt(0)) * 10;
        soma += Integer.parseInt("" + cpf.charAt(1)) * 9;
        soma += Integer.parseInt("" + cpf.charAt(2)) * 8;
        soma += Integer.parseInt("" + cpf.charAt(3)) * 7;
        soma += Integer.parseInt("" + cpf.charAt(4)) * 6;
        soma += Integer.parseInt("" + cpf.charAt(5)) * 5;
        soma += Integer.parseInt("" + cpf.charAt(6)) * 4;
        soma += Integer.parseInt("" + cpf.charAt(7)) * 3;
        soma += Integer.parseInt("" + cpf.charAt(8)) * 2;
        soma = (soma * 10) % 11;
        if (soma != Integer.parseInt("" + cpf.charAt(9)))
            return false;

        soma = Integer.parseInt("" + cpf.charAt(0)) * 11;
        soma += Integer.parseInt("" + cpf.charAt(1)) * 10;
        soma += Integer.parseInt("" + cpf.charAt(2)) * 9;
        soma += Integer.parseInt("" + cpf.charAt(3)) * 8;
        soma += Integer.parseInt("" + cpf.charAt(4)) * 7;
        soma += Integer.parseInt("" + cpf.charAt(5)) * 6;
        soma += Integer.parseInt("" + cpf.charAt(6)) * 5;
        soma += Integer.parseInt("" + cpf.charAt(7)) * 4;
        soma += Integer.parseInt("" + cpf.charAt(8)) * 3;
        soma += Integer.parseInt("" + cpf.charAt(9)) * 2;
        soma = (soma * 10) % 11;
        if (soma != Integer.parseInt("" + cpf.charAt(10)))
            return false;

        return true;
    }
}