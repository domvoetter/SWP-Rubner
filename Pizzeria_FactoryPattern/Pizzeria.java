package Pizzeria_FactoryPattern;

public abstract class Pizzeria {

    abstract Pizza createPizza(String sorte);
    
    public Pizza orderPizza(String sorte)
    {
        Pizza pizza = createPizza(sorte);

        pizza.backen();
        pizza.schneiden();
        pizza.einpacken();

        return pizza;
    }
}
