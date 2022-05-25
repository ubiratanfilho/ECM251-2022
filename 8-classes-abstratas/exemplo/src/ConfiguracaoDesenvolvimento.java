public class ConfiguracaoDesenvolvimento extends Configuracao{
    private String user;

    public ConfiguracaoDesenvolvimento(String bANCO_DE_DADOS_URL, String aPLICACAO_URL) {
        super(bANCO_DE_DADOS_URL, aPLICACAO_URL, true, true);
    }

    public ConfiguracaoDesenvolvimento(String bANCO_DE_DADOS_URL, String aPLICACAO_URL, boolean dEBUG, boolean lOG) {
        super(bANCO_DE_DADOS_URL, aPLICACAO_URL, dEBUG, lOG);
        //TODO Auto-generated constructor stub
    }

    @Override
    public String getUser() {
        // TODO Auto-generated method stub
        return "locahost";
    }

    @Override
    protected boolean setUser(String user) {
        if(user.isEmpty()){
            return false;
        }
        this.user = user;
        return true;
    }

    
    
}
