package com.mangust;

public class Lab3 {
    public static void main(String[] args)
            throws InterruptedException, IllegalArgumentException {
        HouseholdAppliances appliance1 = new HouseholdAppliances(
                "defBrand", "defModel", 1000, 'A');
        appliance1.power();
        appliance1.power();
        System.out.println("appliance1 energyEfficiency: " +
                appliance1.getEnergyEfficiency());
        System.out.println();
        // // Error
        // HouseholdAppliances appliance2 = new HouseholdAppliances(
        // "defBrand", "defModel", 1000, '.');

        Iron iron1 = new Iron("defIronBrand", "defIronModel", 10000, 'B');
        iron1.straightenClothes();
        iron1.power();
        iron1.straightenClothes();
        iron1.power();
        System.out.println("IronSmall watts: " + iron1.getWatts());
        System.out.println();

        TV tv1 = new TV("brand", "model", 100000, 'C', 19);
        System.out.println("TV watts: " + tv1.getWatts());
        System.out.println("TV channel: " + tv1.getChannel());
        tv1.setChannel(10);
        tv1.power();
        System.out.println("TV watts: " + tv1.getWatts());
        tv1.setChannel(11);
        System.out.println("TV channel: " + tv1.getChannel());
        System.out.println("TV is smart: " + TV.isSmart());
        System.out.println();

        Microwave microwave1 = new Microwave(
                "defMicrowaveBrand", "defMicrowaveModel", 1000000, 'D');
        // microwave1.power(-1); // Error
        microwave1.power(3);
        System.out.println();

        TVSmart tvsmart1 = new TVSmart(
                "TVSmart brand", "TVSmart model", 1000000, 'E', 25);
        System.out.println("TVSmart is smart: " + TV.isSmart());
        System.out.println();

        IronEnergyEfficient ironEf1 = new IronEnergyEfficient(
                "defIronEfBrand", "defIronEfModel", 100000, 'A');
        ironEf1.power();
        System.out.println("IronEf watts: " + ironEf1.getWatts());
        ironEf1.straightenClothes();
        ironEf1.power();
        System.out.println();

        IronSmall ironSmall1 = new IronSmall(
                "defIronSmallBrand", "defIronSmallModel", 1000000, 'B');
        ironSmall1.power();
        System.out.println("IronSmall watts: " + ironSmall1.getWatts());
        ironSmall1.straightenClothes();
        ironSmall1.power();
        System.out.println();
    }
}
