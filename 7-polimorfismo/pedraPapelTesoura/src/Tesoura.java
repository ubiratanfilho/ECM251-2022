public class Tesoura extends Jogada {
    public Tesoura() {
        super(enumJogadas.PAPEL, enumJogadas.LAGARTO);
    }

    @Override
    public enumJogadas getTipo() {
        // TODO Auto-generated method stub
        return enumJogadas.TESOURA;
    }

    @Override
    public String toString() {
        String tesoura = """                            
    .......                    
    :--::::::---:                 
.::::...........:::.              
::..................:-.            
.-:............-.=......::.          
::.............:  .........::         
-:.............::  =.........::        
::.............::  .:..........::       
::..............-   .............::      
::..............:.   -.............:.     
.:...............-   -...............-     
:...............=    =.........:::...::    
::..............:.   -........::.  :...:.   
-...............:    :......:-.    -....:   
.:...............:   .:....:-.     =:....:   
:...............-    .:...-.     .-......:.  
:..............::    -..::     .:-........-  
:.............::     =.+      .=..........-  
::.............:      .:      ::...........:. 
-.............:.             =..............: 
-............::           .:-...............: 
-............-           :-.................: 
-...........=            =..................: 
-..........:               -:...............: 
-.........::                ................: 
-........::                 ................: 
::.......:                =.:..............:. 
.:......-                  =...............-  
:.....:.                  .:..............-  
:....:.                   .:.............::  
.:..=:                   :-:.............:   
-:-                    ==...............:   
-.                    -:...............:.   
.                   -.................-    
.                  -:................-     
.               .:.................::     
..:.             .-.................::.:.   
.:-:  .           ::.................::   ::  
.--   ..        .=...................:      -.
.::.     .    .-::..................::        .
..         :  +.....................-.          
.           .-:...................::            
.--..............:-:              
  .:-::::::::::::-.               
   .. .........  ::               

        """;
        return tesoura;
    }
}
