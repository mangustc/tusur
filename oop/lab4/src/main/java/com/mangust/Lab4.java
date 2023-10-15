package com.mangust;

public class Lab4 {
    public static void main(String[] args) {
        IsoscTriangle isoscTriangle = new IsoscTriangle(5, 5, 90);
        EqTriangle eqTriangle = new EqTriangle(5, 5, 60);
        RightTriangle rightTriangle = new RightTriangle(5, 5, 90);

        Picture.printCharacteristics(isoscTriangle, eqTriangle, rightTriangle);
        System.out.println("\n\nArea sum: " + Picture.getSumArea(isoscTriangle, eqTriangle, rightTriangle));
    }
}
