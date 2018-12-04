package RFS;
import jade.core.*;
import java.io.*;
import jade.core.behaviours.CyclicBehaviour;
import java.util.Scanner;
import RFS.ReadAgent;
import jade.*;
import jade.wrapper.*;

public class App extends Agent{
    public String destino = null;
    public Location origen = null;
    public String remoteFile;
    public String localFile;
    public int count = 0;
    
	public void setup(){

        System.out.println("--------------------------------");
        System.out.println("---RFS - AGENTES MOVILES - DS---");
        System.out.println("--------------------------------");
        System.out.println("Se crea al agente --> " + getName());

        Scanner sc = new Scanner(System.in);
        boolean salir = false;
        
        ContainerController container = this.getContainerController();
        
        while (!salir) {
            
            menu();
            int opcion =0;
            opcion = sc.nextInt();

            if(opcion == 1){
                this.setting();
                ReadAgent rd = new ReadAgent(this.destino, this.remoteFile, this.localFile, this.origen);
                try{
                    container.acceptNewAgent("ReadAgent", rd).start();
                    
                }catch(Exception e){
                    System.out.println("Hubo un error al lanzar el agente.");
                }
            }
            if(opcion == 2){
                this.setting();
                WriteAgent wr = new WriteAgent(this.destino, this.remoteFile, this.localFile, this.origen);
                try{
                    container.acceptNewAgent("WriteAgent", wr).start();
                    
                }catch(Exception e){
                    System.out.println("Hubo un error al lanzar el agente.");
                }
            }
            if(opcion == 3){
                System.out.println("SALIR");
            }
        }

    }
    
    public void menu(){

        System.out.println("1 - Read");
        System.out.println("2 - Write");
        System.out.println("3 - Salir");
        System.out.print(">>> ");

    }

    public void setting(){

        Scanner sc = new Scanner(System.in);

        this.setOrigen();

        System.out.println("Ingrese nombre del contenedor al cual migrar !");
        System.out.print(">>> ");
        
        String destino = sc.nextLine();
        this.setDestino(destino);

        System.out.println("Ingrese nombre del archivo remoto !");
        System.out.print(">>> ");

        String rFileName = sc.nextLine();
        this.setRemoteFile(rFileName);

        System.out.println("Ingrese nombre del archivo local !");
        System.out.print(">>> ");

        String lFileName = sc.nextLine();
        this.setLocalFile(lFileName);


    }

    public void setDestino(String destino){
        this.destino = destino;
    }

    public void setOrigen(){
        this.origen = here();
    }

    public void setLocalFile(String filename){
        this.localFile = filename;
    }

    public void setRemoteFile(String filename){
        this.remoteFile = filename;
    }

}
	