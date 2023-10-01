package com.mangust;

public class HouseholdAppliances {
    String brand;
    String model;
    float price;
    char energyEfficiency;

    boolean poweredOn;
    int watts;

    static boolean smart = false;

    public HouseholdAppliances(String brand, String model,
            float price, char energyEfficiency) throws IllegalArgumentException {
        this.brand = brand;
        this.model = model;
        checkPrice(price);
        this.price = price;
        checkEnergyEfficiency(energyEfficiency);
        this.energyEfficiency = energyEfficiency;

        this.poweredOn = false;
        this.watts = 0;
    }

    public void power() {
        if (this.poweredOn)
            System.out.println("Switching off...");
        else
            System.out.println("Switching on...");
        this.poweredOn = !this.poweredOn;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        checkPrice(price);
        this.price = price;
    }

    private static void checkPrice(float price)
            throws IllegalArgumentException {
        if (price < 0)
            throw new IllegalArgumentException(
                    "Price can't be lower than zero");
    }

    public char getEnergyEfficiency() {
        return energyEfficiency;
    }

    private static void checkEnergyEfficiency(char energyEfficiency)
            throws IllegalArgumentException {
        if ('A' > energyEfficiency || 'G' < energyEfficiency)
            throw new IllegalArgumentException(
                    "Energy efficiency should be a symbol from 'A' to 'G'");
    }

    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    public boolean isPoweredOn() {
        return poweredOn;
    }

    public int getWatts() {
        return watts;
    }

    public static boolean isSmart() {
        return smart;
    }
}
