package ListadoCircular;
import jade.core.*;
import jade.core.behaviours.CyclicBehaviour;
import java.util.*;
import javax.sound.midi.MidiDevice.Info;
import jade.lang.acl.*;
import jade.content.*;
import jade.content.onto.basic.*;
import jade.content.lang.sl.*;
import jade.domain.JADEAgentManagement.*;
import jade.domain.mobility.*;

public class ListadoCircular extends Agent {

	public boolean error = false;
	public int operacion = 0;
	public ArrayList containers = new ArrayList<>();  // Obtiene una Lista de los Contenedores registrados en JADE.
	public int cantidad_maxima_contenedores = 0;
	public int cant_contenedores = 0;
	public ArrayList<Informacion> listaInfo = new ArrayList<Informacion>();

    // ContainerID destino = null;
	Location destino= null;
	Location origen = null;
    Location mudarse = null;

    public void setup() {
		
		System.out.println("Se crea al agente --> " + getName()+"\n");

		// Registramos el lenguaje y ontologia para la movilidad del agente.
		getContentManager().registerLanguage(new SLCodec());
	    getContentManager().registerOntology(MobilityOntology.getInstance());

	    origen = here();
		System.out.println("Origen --> " + origen.getName()+"\n");
		
		// Registra el comportamiento deseado del agente
		addBehaviour( 
			new CyclicBehaviour(this) {
				public void action() {
					if (_state == 0) {
							verContainers();
							cantidad_maxima_contenedores = containers.size();
							cant_contenedores = 0;

							if (cantidad_maxima_contenedores != 0)
								_state = 1;
							else
								_state = 2;  
					}
					switch(_state) {
						case 1:
							// ME MUDO A LA SIGUIENTE MAQUINA   
							destino = (Location)containers.get(cant_contenedores);
							++cant_contenedores;
                            System.out.println("Estado 1 --> Comienza la migracion del agente al destino --> " + destino.getName()+"\n");
							
							if(cant_contenedores < cantidad_maxima_contenedores){
                                try {
                                    doMove(destino);
								} catch (Exception e) {
                                    System.out.println("fallo al moverse \n");
                                    e.getMessage();
								}
							
								// Leno la lista (Info) de cada migracion
								Informacion info = new Informacion();		
								info.leerDatos();
								listaInfo.add(info);

                            }else {
                                _state++;
                                try {
                                    System.out.println("regresando a --> " + origen.getID());
                                    doMove(origen);
                                    } catch (Exception e) {
                                    System.out.println("Falla al mover al regresar al origen"); 
                                    e.getMessage();
                                }
                                break;
                            }
							
							break;
						case 2:							
							// Muestra la lista con la info de los contenedores
							for (Informacion i : listaInfo) {
								i.mostrarInfo();
							}
							System.out.println("Estado 2 --> Comienza la auto eliminacion del agente en origen --> " + getName()+"\n");
							try {
								doDelete();
								System.out.println("Despues de la auto eliminacion del agente Estado 2 --> " + getName() +"\n");
							} catch (Exception e) {
								System.out.println("fallo al moverse al Destino \n");
								e.getMessage();
							}
							break; 									
					}
				}
				private int _state = 0; // variable de maquina de estados del agente
			}
		);
	}

	//Metodo para actualizar a lista de containers disponibles
	protected void actualizarContainers() {	 	
		getContentManager().registerLanguage(new SLCodec());
	    getContentManager().registerOntology(MobilityOntology.getInstance());
	    
	    //origen = here();
	    containers.clear();
	    ACLMessage request= new ACLMessage(ACLMessage.REQUEST);
	    request.setLanguage(new SLCodec().getName());
	    
	    // Establecemos que MobilityOntology sea la ontologia de este mensaje.
	    request.setOntology(MobilityOntology.getInstance().getName());
	    
	    // Solicitamos a AMS una lista de containers disponibles
	    Action action= new Action(getAMS(), new QueryPlatformLocationsAction());
	    
	    try	{
            getContentManager().fillContent(request, action);
            request.addReceiver(action.getActor());
            send(request);
        
            // Filtramos los mensajes INFORM que llegan desde el AMS
            MessageTemplate mt= MessageTemplate.and(MessageTemplate.MatchSender(getAMS()), MessageTemplate.MatchPerformative(ACLMessage.INFORM));
        
            ACLMessage resp= blockingReceive(mt);
            ContentElement ce= getContentManager().extractContent(resp);
            Result result=(Result) ce;
            jade.util.leap.Iterator it= result.getItems().iterator();
            // Almacena un ArrayList "Locations" de "Containers" donde puede moverse el agente movil.
            
            while(it.hasNext()) {
                Location loc=(Location) it.next();
                containers.add(loc);
            }
	    } catch(Exception ex) {  
            ex.printStackTrace();
        }
	}	
	
	protected void verContainers() {
	    //ACTUALIZAR
	    actualizarContainers();
	    //VISUALIZAR
	    System.out.println("******Containers disponibles: *******\n");
	    for(int i=0; i<containers.size(); i++) {
	      System.out.println("    ["+ i + "] " + ((Location)containers.get(i)).getName());
	    }
	    System.out.println("\n");
	}
}	