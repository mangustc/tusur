package com.mangust;

public class IronEnergyEfficient extends Iron {
    int workingWatts = 800;

    public IronEnergyEfficient(String brand, String model,
            float price, char energyEfficiency) throws IllegalArgumentException {
        super(brand, model, price, energyEfficiency);
    }

    @Override
    public void power() {
        if (this.poweredOn) {
            System.out.println("*turned off sound*not hot anymore");
            this.watts = 0;
        } else {
            System.out.println("*turn on sound*becoming hot");
            this.watts = this.workingWatts;
        }
        this.poweredOn = !this.poweredOn;
    }
}
