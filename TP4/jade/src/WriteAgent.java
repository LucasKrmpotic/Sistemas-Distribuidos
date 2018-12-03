package RFS;
import jade.core.*;
import java.io.*;
import jade.core.behaviours.CyclicBehaviour;
import java.util.Scanner;
import jade.content.*;
import jade.domain.JADEAgentManagement.*;

public class WriteAgent extends Agent{
    
    private final int MAX_BUFFER = 1024;
    
    public String destinoName;
    public Location origen = null;
    public String remoteFile;
    public String localFile;
    public ContainerID destino;
    public byte[] buffer;
    FileInputStream in = null;
    FileOutputStream out = null;

    int length = 0;
    
    // Constructor
    public WriteAgent(String destino, String remoteFile, String localFile, Location origen){
        
        this.destinoName = destino;
        this.origen = origen;
        this.localFile = localFile;
        this.remoteFile = remoteFile;
        this.buffer = new byte[MAX_BUFFER];
        this.in = new FileInputStream(localFile);
        this.out = new FileOutputStream(remoteFile, true);

    }

	public void setup(){

        System.out.println("Se crea al agente --> " + getName());
        
        // inicializa origen y destino
        this.destino = new ContainerID(this.destinoName, null);

         System.out.println("Origen --> " + this.origen.getID()); 
		System.out.println("Destino --> " + this.destino.getID());
        
        // registra el comportamiento deseado del agente
        addBehaviour(new CyclicBehaviour(this){
			public void action() {
                
                switch(_state){
                    case 0:
                    // Comienza la migración del agente al destino
                        _state++;
                        System.out.println("Estado 0 Comienza la migración del agente al destino --> " + destino.getID());
                        // Debo Leer del archivo local
                        try {
                            length = in.read(buffer);
                            System.out.println("Leyendo " + length + " Bytes.");
                        } catch (Exception e) {
                            e.getMessage();
                        }
                        try {
                            System.out.println("Comienza la migracion a destino" + destino.getID());
                            doMove(destino);
                        } catch (Exception e) {
                            System.out.println("fallo al moverse al Container destino");
                            e.getMessage();
                        }
                        break;
                    case 1:
                    // el agente llegó al destino, recupera el directorio y regresa
                        if (length > 0) {
                            try {
                                out.write(buffer);
                                System.out.println("Escribiendo " + length + " Bytes.");
                            } catch(Exception e){
                                e.getMessage();
                            }

                            try {
                                doMove(destino);
                            } catch(Exception e){
                                e.printStackTrace();
                            }
                            _state--;
                        }
                        else {
                            System.out.println("No tengo más para leer");
                            _state++;
                        }
                        break;
                    case 2:
                        // Regresó al origen, imprime el directorio y destruye al agente
                        System.out.println("Estado 2 Regresó a origen --> " + here().getID());
                        try {
                            in.close();
                            out.close();
                        } catch(Exception e){
                            e.printStackTrace();
                        }
                        
                        // destruye al agente
                        System.out.println("destruye al agente --> " + getName());
                        doDelete();
                        break;
                    default:
                        myAgent.doDelete();
                    }
			    }
			private int _state = 0; // variable de máquina de estados del agente
		});
        // registra un comportamiento dummy a los efectos de verificar concurrencia y movilidad
        addBehaviour(new CyclicBehaviour(this){
                
            public void action() 
            {
                // arranca muestra cartel, duerme 5 segundos y muestra otro cartel
                _contador++;
                
                }

            private int _contador = 0; // cuenta la cantidad de ciclos en que se ejecuta el comportamiento
        
        });
        }

        // Luego de ser movido el agente ejecuta este código
        protected void afterMove() {
        System.out.println("Siempre ejecuta afterMove cuando al llegar --> " + here().getID());
        }
    


}
