package com.mangust;

public class ComputerMonitor extends Computer {
    int monitorSize;

    ComputerMonitor() {
        super();
        this.monitorSize = 0;
    }

    ComputerMonitor(String brand, int price, int hddSizeMb, int monitorSize)
            throws IllegalArgumentException {
        super(brand, price, hddSizeMb);
        if (monitorSize < 0)
            throw new IllegalArgumentException(
                    "Monitor size can't be lower than zero");
        this.monitorSize = monitorSize;
    }

    public void print() {
        System.out.println("ComputerMonitor:");
        System.out.println("\tbrand: " + this.brand);
        System.out.println("\tprice: " + this.price);
        System.out.println("\thddSizeMb: " + this.hdd.getSizeMb());
        System.out.println("\tmonitorSize: " + this.monitorSize);
    }
}
