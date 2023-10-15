package com.mangust;

public class TVSmart extends TV {
    static boolean smart = true;

    public TVSmart(String brand, String model, float price,
            char energyEfficiency, float size) throws IllegalArgumentException {
        super(brand, model, price, energyEfficiency, size);
    }

    public static boolean isSmart() {
        return smart;
    }
}
