package com.mangust;

public class BinaryString {
    String binary;

    BinaryString(String binary) throws IllegalArgumentException{
        int stringLength = binary.length();
        for (int i = 0; i < stringLength; i++) {
            switch (binary.charAt(i)) {
                case '0', '1':
                    break;

                default:
                    throw new IllegalArgumentException("Binary should only contain numbers 1 and 0");
            }
        }
        this.binary = binary;
    }

    public int toDecimalNum() {
        return Integer.parseInt(this.binary, 2);
    }

    public void add(int num) {
        this.binary = Integer.toBinaryString(num + Integer.parseInt(this.binary, 2));
    }

    public void add(BinaryString binaryNumString) {
        this.binary = Integer.toBinaryString(Integer.parseInt(binaryNumString.binary, 2) + Integer.parseInt(this.binary, 2));
    }

    public void sub(int num) {
        this.binary = Integer.toBinaryString(Integer.parseInt(this.binary, 2) - num);
    }

    public void sub(BinaryString binaryNumString) {
        this.binary = Integer.toBinaryString(Integer.parseInt(this.binary, 2) - Integer.parseInt(binaryNumString.binary, 2));
    }

    public void multiply(int num) {
        this.binary = Integer.toBinaryString(Integer.parseInt(this.binary, 2) * num);
    }

    public void multiply(BinaryString binaryNumString) {
        this.binary = Integer.toBinaryString(Integer.parseInt(this.binary, 2) * Integer.parseInt(binaryNumString.binary, 2));
    }

    public void divide(int num) {
        this.binary = Integer.toBinaryString(Integer.parseInt(this.binary, 2) / num);
    }

    public void divide(BinaryString binaryNumString) {
        this.binary = Integer.toBinaryString(Integer.parseInt(this.binary, 2) / Integer.parseInt(binaryNumString.binary, 2));
    }
}
