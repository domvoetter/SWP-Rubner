package Pizzeria_FactoryPattern;

public class BerlinPizzeria extends Pizzeria{

    @Override
    Pizza createPizza(String sorte) {
        switch(sorte)
        {
            case "Salami": return new BerlinSalami();
            case "Hawaii": return new BerlinHawaii();
            case "QuattroStagioni": return new BerlinQuattroStagioni();
            case "Calzone": return new BerlinCalzone();
            default: return null;
        }
    }

    
    
}
