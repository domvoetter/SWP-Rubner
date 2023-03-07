package Pizzeria_FactoryPattern;

public class RohstockCalzone extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rohstocker Calzone wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rohstocker Calzone wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rohstocker Calzone wurde eingepackt");
    }
    
}
