package com.mangust;

public class Microwave extends HouseholdAppliances {
    public Microwave(String brand, String model,
            float price, char energyEfficiency) throws IllegalArgumentException {
        super(brand, model, price, energyEfficiency);
    }

    // @Override
    public void power(int seconds)
            throws InterruptedException, IllegalArgumentException {
        if (seconds < 0)
            throw new IllegalArgumentException(
                    "Seconds amount can't be lower than zero");
        if (!this.poweredOn)
            this.poweredOn = true;
        for (int sec = 1; sec <= seconds; sec++) {
            Thread.sleep(1000);
            System.out.println("Heating up the food " +
                    ((float) sec / (float) seconds) * 100 + "%");
        }
    }
}
