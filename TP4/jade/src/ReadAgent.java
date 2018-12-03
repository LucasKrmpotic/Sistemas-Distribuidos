package RFS;
import jade.core.*;
import java.io.*;
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
    public int count;
    public byte[] buffer;
    public FileInputStream in = null;
    public FileOutputStream out = null;


    // Constructor
    public ReadAgent(String destino, String remoteFile, String localFile, Location origen){
        
        this.destinoName = destino;
        this.origen = origen;
        this.localFile = localFile;
        this.remoteFile = remoteFile;
        this.destino = null;
        this.buffer = new byte[MAX_BUFFER];
        this.in = new FileInputStream(localFile);
        this.out = new FileOutputStream(remoteFile);

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
                            Thread.sleep(3000);
                            System.out.println("Despues de doMove en CyclicBehaviour de Estado 0 --> " + destino.getID());
                        } catch (Exception e) {
                            System.out.println("fallo al moverse al Container destino");
                            e.getMessage();
                        }
                        break;
                    case 1:
                    // el agente llegó al destino, recupera el directorio y regresa
                        _state++;
                        System.out.println("Estado 1 agente llegó a destino, realiza la operacion y regresa a --> " + origen.getID());
                        
                        try {
                            Thread.sleep(3000);
                        } catch (Exception e) {
                            e.printStackTrace();
                        }

                        // regresa al origen e imprime el directorio
                        try {
                            System.out.println("regresando a --> " + origen.getID());
                            doMove(origen);
                            System.out.println("despues de domove en CyclicBehaviour estado 1 --> " + here().getID());
                        } catch (Exception e) {
                            System.out.println("Falla al mover al regresar al origen"); 
                            e.getMessage();
                        }
                        // Leer el archivo (tamaño del buffer)
                        break;
                    case 2:
                        // Estoy en el origen
                        // escribir archivo local (tamaño del buffer)
                        // _state--; para volver al estado anterior de la maquina de estados
                        // _state++; cuando termine de escribir el archivo
                    case 3:
                        // Regresó al origen, imprime el directorio y destruye al agente
                        System.out.println("Estado 2 Regresó a origen --> " + here().getID());
                        
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

    }

    


}
