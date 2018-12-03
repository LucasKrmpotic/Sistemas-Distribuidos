package ListadoCircular;
import java.io.Serializable;
import java.net.InetAddress;
import java.util.*;

public class Informacion implements Serializable{
    public String ip;
    public String hostName;
    public String timeLlegada;
    public String timePartida;
    public String so;

    public Informacion (){
        this.timeLlegada = "";
        this.timePartida = "";
        this.ip = "";
        this.so = ""; 
        this.hostName = "";
    }

    public void leerDatos(){
        System.out.println("------------------------------------------");
        // Lectura de SO
        this.so = System.getProperty("os.name");
        // Lectura de host name y direccion ip
        try {
            this.ip = InetAddress.getLocalHost().getHostAddress();   
            this.hostName = InetAddress.getLocalHost().getHostName();        
        } catch (Exception e) {
            e.printStackTrace();
        }
        // Fecha del contenedor
        Calendar calendario = Calendar.getInstance();
        this.timeLlegada = String.valueOf(calendario.getTime());
        try {
            Thread.sleep(5000);
        } catch (Exception e) {
            e.printStackTrace();
        }
        Calendar cal = Calendar.getInstance();
        this.timePartida = String.valueOf(cal.getTime());
    }

    public void mostrarInfo(){
        System.out.println("-------------------------------------------------");
        System.out.println("Host Name: " + this.hostName);
        System.out.println("IP: " + this.ip);
        System.out.println("SO: " + this.so);
        System.out.println("Hora Llegada a Destino: " + this.timeLlegada );
        System.out.println("Hora de Partida hacia el Origen: " + this.timePartida);
        System.out.println("-------------------------------------------------");
    }

}

