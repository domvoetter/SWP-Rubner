package Pizzeria_FactoryPattern;

public class BerlinSalami extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Berliner Salami wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Berliner Salami wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Berliner Salami wurde eingepackt");
    }
    
}
