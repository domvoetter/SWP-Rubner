package Pizzeria_FactoryPattern;

public class RohstockPizzeria extends Pizzeria{

    @Override
    Pizza createPizza(String sorte) {
        switch(sorte)
        {
            case "Salami": return new RohstockSalami();
            case "Hawaii": return new RohstockHawaii();
            case "QuattroStagioni": return new RohstockQuattroStagioni();
            case "Calzone": return new RohstockCalzone();
            default: return null;
        }
    }
    
}
