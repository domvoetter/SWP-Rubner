package Pizzeria_FactoryPattern;

public class HamburgHawaii extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Hamburger Hawaii wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Hamburger Hawaii wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Hamburger Hawaii wurde eingepackt");
    }
    
}
