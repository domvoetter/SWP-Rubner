package Pizzeria_FactoryPattern;

public class RostockQuattroStagioni extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rostocker Quattro Stagioni wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rostocker Quattro Stagioni wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rostocker Quattro Stagioni wurde eingepackt");
    }
    
}
