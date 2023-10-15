package com.mangust;

public class Computer {
    HardDrive hdd;
    String brand;
    int price;

    Computer() {
        this("defaultBrand", 0, 0);
    }

    Computer(String brand, int price, int hddSizeMb)
            throws IllegalArgumentException {
        if (price < 0)
            throw new IllegalArgumentException("price can't be lower than zero");
        this.brand = brand;
        this.price = price;
        this.hdd = new HardDrive(hddSizeMb);
    }

    public HardDrive getHdd() {
        return hdd;
    }

    public String getBrand() {
        return brand;
    }

    public int getPrice() {
        return price;
    }

}
