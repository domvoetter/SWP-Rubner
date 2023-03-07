package Pizzeria_FactoryPattern;

public class HamburgCalzone extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Hamburger Calzone wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Hamburger Calzone wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Hamburger Calzone wurde eingepackt");
    }
    
}
