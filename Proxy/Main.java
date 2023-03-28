package Proxy;

public class Main {
    public static void main(String[] args) {
        Printer blackAndWhitePrinter = new BlackAndWhitePrinter();
        Printer colorPrinter = new ColorPrinter();
        Printer proxy = new PrinterProxy(blackAndWhitePrinter);

        proxy.print("Document 1");
        proxy.switchTo(colorPrinter);
        proxy.print("Document 2");
        proxy.switchTo(blackAndWhitePrinter);
        proxy.print("Document 3");
    }
}
