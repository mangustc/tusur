package com.mangust;

public class TV extends HouseholdAppliances {
    float size;
    int channel;

    public TV(String brand, String model, float price,
            char energyEfficiency, float size) throws IllegalArgumentException {
        super(brand, model, price, energyEfficiency);
        checkSize(size);
        this.size = size;
        this.channel = 1;
    }

    @Override
    public void power() {
        if (this.poweredOn) {
            System.out.println("*turned off sound*Screen turnes black");
            this.watts = 0;
        } else {
            System.out.println("*turn on sound*Screen lights up");
            this.watts = 200;
        }
        this.poweredOn = !this.poweredOn;
    }

    public float getSize() {
        return size;
    }

    private static void checkSize(float size) throws IllegalArgumentException {
        if (size < 0)
            throw new IllegalArgumentException(
                    "TV size can't be lower than zero");
    }

    public int getChannel() {
        return channel;
    }

    public void setChannel(int channel) throws IllegalArgumentException {
        checkChannel(channel);
        if (!this.poweredOn) {
            System.out.println("The TV is not on");
            return;
        }
        this.channel = channel;
    }

    private static void checkChannel(int channel)
            throws IllegalArgumentException {
        if (channel < 1)
            throw new IllegalArgumentException(
                    "Channel number must be higher than zero");
    }
}
