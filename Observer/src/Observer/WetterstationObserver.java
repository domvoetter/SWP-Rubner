package Observer;

public class WetterstationObserver implements Observer{
	
	@Override
    public void pushTemp(int state) { 
        System.out.println("Temp is updated with "+state); 
    }

	@Override
	public void pushHum(int state) {
		 System.out.println("Hum is updated with "+state); 
		
	} 
	
}
