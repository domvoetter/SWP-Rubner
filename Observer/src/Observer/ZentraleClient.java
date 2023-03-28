package Observer;

public class ZentraleClient {

	public static void main(String[] args) { 
        ConcreteSubject concreteSubject = new ConcreteSubject(); 
        concreteSubject.register(new WetterstationObserver()); 

        concreteSubject.setState(30, 15); 
        concreteSubject.setState(40, 25); 
    } 

}
