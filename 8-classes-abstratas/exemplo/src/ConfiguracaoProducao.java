public class ConfiguracaoProducao extends Configuracao {
    private String currentUser;

    public ConfiguracaoProducao(String bANCO_DE_DADOS_URL, String aPLICACAO_URL,
            String currentUser) {
        super(bANCO_DE_DADOS_URL, aPLICACAO_URL, false, true);
        this.currentUser = currentUser;
    }

    @Override
    public String getUser() {
        return currentUser;
    }

    @Override
    protected boolean setUser(String user) {
        if (user.isEmpty()) {
            return false;
        }
        this.currentUser = user;
        return true;
    }
    
    
}
