package Pizzeria_FactoryPattern;

public class HamburgSalami extends Pizza {

    @Override
    void backen()
    {
        System.out.println("Diese Hamburger Salami wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Hamburger Salami wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Hamburger Salami wurde eingepackt");
    }
    
}
