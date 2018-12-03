package RFS;
import jade.core.*;
import java.io.*;
import jade.core.behaviours.CyclicBehaviour;
import java.util.*;
import jade.content.*;
import jade.domain.JADEAgentManagement.*;
import java.io.FileInputStream;
import java.io.FileOutputStream;

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

    int count = 0;
	long offset = 0;
    
    // Constructor
    public WriteAgent(String destino, String remoteFile, String localFile, Location origen){
        
        this.destinoName = destino;
        this.origen = origen;
        this.localFile = localFile;
        this.remoteFile = remoteFile;
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
                        // Debo Leer del archivo local
                        try {
                            System.out.println("Archivo Local:"+ localFile);
                            File _fr = new File(localFile);
                            if (!_fr.exists()){
                                System.out.println("No existe el archivo:"+_fr.getName());
                            }
                            FileInputStream fin = new FileInputStream(_fr.toPath().toString());
                            if (offset > 0){
                                fin.skip(offset);
                            }
                            Arrays.fill(buffer, (byte)'0');
                            count = fin.read(buffer);
                            fin.close();
                            System.out.println("Leyendo " + count + "Bytes");
                            offset = offset + count;

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
                         
                         if (count > 0) {
                            try {
                                System.out.println("Archivo Remoto:"+ remoteFile);
                                File _fl = new File(remoteFile);

                                if (!_fl.exists())
                                    _fl.createNewFile();

                                FileOutputStream fout = new FileOutputStream(_fl.toPath().toString(), true);

                                fout.write(buffer);
                                fout.close();
                                System.out.println("Escribiendo " + count + " Bytes");
                            } catch(Exception e){
                                e.printStackTrace();
                            }

                            try {
                                doMove(origen);
                            } catch(Exception e){
                                e.printStackTrace();
                            }
                            _state--;
                        } else {
                            _state++;
                            System.out.println("No hay mas para Leer");
                        }
                        break;
                    case 2:
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

        
    


}
