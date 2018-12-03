package ListadoCircular;
import java.net.InetAddress;
import java.util.*;

public class Info {
    public String ip;
    public String hostName;
    public String hora;
    public String minutos;
    public String segundos;
    public String so;

    public Info (){
        this.hora = "";
        this.minutos = "";
        this.segundos = "";
        this.ip = "";
        this.so = ""; 
        this.hostName = "";
    }

    public void leerDatos(){
        // Lectura de SO
        this.so = System.getProperty("os.name");
        // Lectura de host name y direccion ip
        this.ip = InetAddress.getLocalHost().getHostAddress();   
        this.hostName = InetAddress.getLocalHost().getHostName();
        // Fecha del contenedor
        Calendar calendario = Calendar.getInstance();
        this.hora = calendario.get(Calendar.HOUR_OF_DAY);
        this.minutos = calendario.get(Calendar.MINUTE);
        this.segundos = calendario.get(Calendar.SECOND);
    }

    public void mostrarInfo(){
        System.out.println("Host Name: " + this.hostName);
        System.out.println("IP: " + this.ip);
        System.out.println("SO: " + this.so);
        System.out.println("Hora Llegada a Destino: " + this.hora + ":" + this.minutos + ":" + this.segundos );
    }

    public static void main(String[] args) {
        Info info = new Info();
        info.leerDatos();
        info.mostrarInfo();
    }
}

