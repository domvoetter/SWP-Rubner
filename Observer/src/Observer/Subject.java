package Observer;

import java.util.ArrayList;
import java.util.List;

public abstract class Subject { 

    private final List<Observer> observerList = new ArrayList<Observer>(); 

    public void register(Observer newObserver){ 
        observerList.add(newObserver); 
    } 

    public void unregister(Observer newObserver){ 
        observerList.remove(newObserver); 
    } 

    protected void notifyObservers(int temp, int hum){ 
        for (Observer observer : observerList) { 
            observer.pushTemp(temp); 
            observer.pushHum(hum);
        } 
    } 
}  