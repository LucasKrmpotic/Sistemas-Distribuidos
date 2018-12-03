package RFS;
import jade.core.*;
import java.io.*;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import jade.core.behaviours.CyclicBehaviour;
import java.util.Scanner;
import jade.content.*;
import jade.domain.JADEAgentManagement.*;

public class ReadAgent extends Agent{
    
    private final int MAX_BUFFER = 1024;
    
    public String destinoName;
    public Location origen = null;
    public String remoteFile;
    public String localFile;
    public ContainerID destino;
    public byte[] buffer;
    
    FileInputStream in = null;
    FileOutputStream out = null;
   
    int count = 0;
	long offset = 0;

    // Constructor
    public ReadAgent(String destino, String remoteFile, String localFile, Location origen){
        
        this.destinoName = destino;
        this.origen = origen;
        this.localFile = localFile;
        this.remoteFile = "/Documentos/" + remoteFile;
        this.destino = null;
        this.buffer = new byte[MAX_BUFFER];
        
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
                        try {
                            doMove(destino);
                            System.out.println("Despues de doMove en CyclicBehaviour de Estado 0 --> " + destino.getID());
                        } catch (Exception e) {
                            System.out.println("fallo al moverse al Container destino");
                            e.getMessage();
                        }
                        break;
                    case 1:
                    // el agente llegó al destino, recupera el directorio y regresa
                        _state++;
                        System.out.println("Estado 1 agente llegó a destino, lee de archivo y regresa a --> " + origen.getID());
                        try {
                            if (in == null){
                                in = new FileInputStream(remoteFile);
                            }
                            in.skip(offset);
                            count = in.read(buffer);
                            System.out.println("Leyendo " + count + "Bytes");
                            offset = offset + count;

                        } catch (Exception e) {
                            e.getMessage();
                        }
                                              
                        // regresa al origen
                        try {
                            System.out.println("regresando a --> " + origen.getID());
                            doMove(origen);
                            System.out.println("despues de domove en CyclicBehaviour estado 1 --> " + here().getID());
                        } catch (Exception e) {
                            System.out.println("Falla al mover al regresar al origen"); 
                            e.getMessage();
                        }
                        break;
                    case 2:
                        // Estoy en el origen
                        // escribir archivo local
                        if (count != -1) {
                            try {
                                if (out == null){
                                    out = new FileOutputStream(localFile, true);
                                }
                                out.write(buffer);
                                System.out.println("Escribiendo " + count + " Bytes");
                            } catch(Exception e){
                                e.printStackTrace();
                            }

                            try {
                                doMove(destino);
                            } catch(Exception e){
                                e.printStackTrace();
                            }
                            _state--;
                        } else {
                            _state++;
                            System.out.println("No hay mas para Leer");
                        }
                    case 3:
                        // Cierro el in y out
                        try {
                            in.close();
                            out.close();
                        } catch (Exception e) {
                            e.getMessage();
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
            _contador++;
            
            }

        private int _contador = 0; // cuenta la cantidad de ciclos en que se ejecuta el comportamiento
    
    });
    }
}
