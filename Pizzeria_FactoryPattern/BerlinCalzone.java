package Pizzeria_FactoryPattern;

public class BerlinCalzone extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Berliner Calzone wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Berliner Calzone wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Berliner Calzone wurde eingepackt");
    }
    
}
