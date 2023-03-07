package Pizzeria_FactoryPattern;

public class HamburgQuattroStagioni extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Hamburger Quattro Stagioni wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Hamburger Quattro Stagioni wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Hamburger Quattro Stagioni wurde eingepackt");
    }
    
}
