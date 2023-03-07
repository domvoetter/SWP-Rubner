package Pizzeria_FactoryPattern;

public class RostockPizzeria extends Pizzeria{

    @Override
    Pizza createPizza(String sorte) {
        switch(sorte)
        {
            case "Salami": return new RostockSalami();
            case "Hawaii": return new RostockHawaii();
            case "QuattroStagioni": return new RostockQuattroStagioni();
            case "Calzone": return new RostockCalzone();
            default: return null;
        }
    }
    
}
