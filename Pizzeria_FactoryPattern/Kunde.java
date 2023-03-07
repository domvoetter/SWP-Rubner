package Pizzeria_FactoryPattern;

import java.util.Scanner;

import javax.swing.DefaultBoundedRangeModel;

public class Kunde {

    static Pizza mach(String standort, String sorte)
    {
        Pizzeria berlin = new BerlinPizzeria();
        Pizzeria hamburg = new HamburgPizzeria();
        Pizzeria rostock = new RostockPizzeria();

        switch(standort)
        {
            case "Berlin": return berlin.orderPizza(sorte);
            case "Hamburg": return hamburg.orderPizza(sorte);
            case "Rostock": return rostock.orderPizza(sorte);
            default: return null;
        }
    }

    public static void main(String[] args) {

        System.out.println("Wo möchten Sie eine Pizza bestellen? ");
        Scanner scanner = new Scanner(System.in);
        String standort = scanner.nextLine();
        System.out.println("Welche Pizza möchten Sie haben? ");
        String sorte = scanner.nextLine();
        Pizza pizza = mach(standort, sorte);

        System.out.println("\n Fertig!");
        System.out.println(pizza);
    }
    
}
