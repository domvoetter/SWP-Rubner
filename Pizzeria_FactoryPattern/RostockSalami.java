package Pizzeria_FactoryPattern;

public class RostockSalami extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rostocker Salami wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rostocker Salami wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rostocker Salami wurde eingepackt");
    }
    
}
