package Pizzeria_FactoryPattern;

public class RohstockHawaii extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rohstocker Hawaii wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rohstocker Hawaii wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rohstocker Hawaii wurde eingepackt");
    }
    
}
