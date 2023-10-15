package com.mangust;

public class Lab8 {
    public static void main(String[] args) {
        BinaryString binaryString1 = new BinaryString("1001");
        System.out.println("binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());

        binaryString1.add(3);
        System.out.println("addDecimal 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());
        binaryString1.add(new BinaryString("1001"));
        System.out.println("addBinary 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());

        binaryString1.sub(3);
        System.out.println("\nsubDecimal 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());
        binaryString1.sub(new BinaryString("1001"));
        System.out.println("subBinary 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());

        binaryString1.multiply(3);
        System.out.println("\nmultiplyDecimal 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());
        binaryString1.multiply(new BinaryString("1001"));
        System.out.println("multiplyBinary 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());

        binaryString1.divide(3);
        System.out.println("\ndivideDecimal 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());
        binaryString1.divide(new BinaryString("1001"));
        System.out.println("divideBinary 3, binary to decimal: " + binaryString1.binary + " to " + binaryString1.toDecimalNum());

        // Error but we catch it
        try {
            BinaryString binaryStringError1 = new BinaryString("00012121");
        } catch (IllegalArgumentException error) {
            System.out.println("\nYou may have entered a non-binary");
        } finally {
            System.out.println("\nMoves past either way");
        }

        // Error!!!
        BinaryString binaryStringError2 = new BinaryString("1111010101021010012010010010");
        System.out.println(binaryStringError2.toDecimalNum());

        // This will not execute
        BinaryString binaryString2 = new BinaryString("1001");
        System.out.println("binary to decimal: " + binaryString2.binary + " to " + binaryString2.toDecimalNum());
    }
}
