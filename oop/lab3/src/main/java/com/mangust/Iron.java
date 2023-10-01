package com.mangust;

public class Iron extends HouseholdAppliances {
    int workingWatts = 1200;

    public Iron(String brand, String model,
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

    public void straightenClothes() throws InterruptedException {
        if (!this.poweredOn) {
            System.out.println("Can't straighten clothes. Iron is off");
            return;
        }
        for (int sec = 1; sec <= 2; sec++) {
            Thread.sleep(1000);
            System.out.println("Clothes straightened " +
                    sec * 50 + "%");
        }
    }

}
