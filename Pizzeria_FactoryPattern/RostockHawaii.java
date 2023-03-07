package Pizzeria_FactoryPattern;

public class RostockHawaii extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rostocker Hawaii wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rostocker Hawaii wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rostocker Hawaii wurde eingepackt");
    }
    
}
