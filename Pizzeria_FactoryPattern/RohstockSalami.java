package Pizzeria_FactoryPattern;

public class RohstockSalami extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rohstocker Salami wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rohstocker Salami wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rohstocker Salami wurde eingepackt");
    }
    
}
