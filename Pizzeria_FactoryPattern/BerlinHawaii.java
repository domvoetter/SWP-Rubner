package Pizzeria_FactoryPattern;

public class BerlinHawaii extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Berliner Hawaii wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Berliner Hawaii wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Berliner Hawaii wurde eingepackt");
    }
    
}
