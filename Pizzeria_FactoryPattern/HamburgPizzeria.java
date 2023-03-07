package Pizzeria_FactoryPattern;

public class HamburgPizzeria extends Pizzeria{

    @Override
    Pizza createPizza(String sorte) {
        switch(sorte)
        {
            case "Salami": return new HamburgSalami();
            case "Hawaii": return new HamburgHawaii();
            case "QuattroStagioni": return new HamburgQuattroStagioni();
            case "Calzone": return new HamburgCalzone();
            default: return null;
        }
    }
    
}
