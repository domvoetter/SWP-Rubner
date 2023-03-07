package Pizzeria_FactoryPattern;

public class RohstockQuattroStagioni extends Pizza{

    @Override
    void backen()
    {
        System.out.println("Diese Rohstocker Quattro Stagioni wurde gebacken");
    }

    @Override
    void schneiden()
    {
        System.out.println("Diese Rohstocker Quattro Stagioni wurde geschnitten");
    }

    @Override
    void einpacken()
    {
        System.out.println("Diese Rohstocker Quattro Stagioni wurde eingepackt");
    }
    
}
