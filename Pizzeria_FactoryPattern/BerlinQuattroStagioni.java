package Pizzeria_FactoryPattern;

public class BerlinQuattroStagioni extends Pizza {

    @Override
    void backen()
    {
        System.out.println("Diese Berliner Quattro Stagioni wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Berliner Quattro Stagioni wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Berliner Quattro Stagioni wurde eingepackt");
    }
    
}
