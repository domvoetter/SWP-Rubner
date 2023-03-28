package Proxy;

class PrinterProxy implements Printer {
    private Printer printer;

    public PrinterProxy(Printer printer) {
        this.printer = printer;
    }

    @Override
    public void print(String document) {
        this.printer.print(document);
    }

    public void switchTo(Printer printer) {
        this.printer = printer;
    }
}
