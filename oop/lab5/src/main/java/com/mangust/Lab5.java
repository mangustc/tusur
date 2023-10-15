package com.mangust;

import java.util.concurrent.ThreadLocalRandom;

public class Lab5 {
    static int[] getRandomDayType() {
        int[] dayType = new int[30];
        for (int i = 0; i < 30; i++)
            dayType[i] = ThreadLocalRandom.current().nextInt(0, 2);
        return dayType;
    }

    static int[] getRainyDayType() {
        int[] dayType = new int[30];
        for (int i = 0; i < 30; i++)
            dayType[i] = 1;
        return dayType;
    }

    static int[] getSunnyDayType() {
        int[] dayType = new int[30];
        return dayType;
    }

    static String getArrayString(int[] arr) {
        String out = "";

        out += "[ ";
        for (int i = 0; i < arr.length - 1; i++)
            out += arr[i] + ", ";
        out += arr[arr.length - 1] + " ]";

        return out;
    }

    public static void main(String[] args) {
        int[] dayType = getRandomDayType();
        // int[] dayType = getRainyDayType();
        // int[] dayType = getSunnyDayType();
        double aCm = 0.0;
        double bM = 0.3;

        System.out.println("dayType: " + getArrayString(dayType));
        
        double positionCm = aCm;
        
        for (int i = 0; i < dayType.length; i++) {
            if (dayType[i] == 0)
                positionCm += 2;
            else 
                positionCm--;

            if (positionCm < aCm)
                positionCm = aCm;
            if (positionCm > bM * 100.0)
                positionCm = bM * 100.0;
        }

        if (positionCm == bM * 100.0)
            System.out.println("The snail climed the tree!");
        else if (positionCm == aCm)
            System.out.println("The snail fell down...");
        else
            System.out.println("The snail climbed " + positionCm / bM + "% of the tree.");
    }
}
