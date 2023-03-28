package Observer;

public class ConcreteSubject extends Subject { 

    private int temp;
    private int hum;

    public void setState(int temp, int hum) { 
        this.temp = temp; 
        this.hum = hum;
        notifyObservers(temp, hum); 
    } 

    public int getTemp() { 
        return temp; 
    } 
    public int getHum() { 
        return hum; 
    } 

} 
