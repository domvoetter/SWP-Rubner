package Pizzeria_FactoryPattern;

public class RostockCalzone extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rostocker Calzone wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rostocker Calzone wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rostocker Calzone wurde eingepackt");
    }
    
}
