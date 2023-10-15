package com.mangust;

public interface Picture {
    static void printCharacteristics(IsoscTriangle isoscTriangle, EqTriangle eqTriangle, RightTriangle rightTriangle) {
        System.out.printf("IsoscTriangle:\n\ta: %f, b: %f, angle: %f\n\tarea: %f\n\tperimeter: %f\n",
            isoscTriangle.a, isoscTriangle.b, isoscTriangle.angle, isoscTriangle.getArea(), isoscTriangle.getPerimeter());
        System.out.printf("EqTriangle:\n\ta: %f, b: %f, angle: %f\n\tarea: %f\n\tperimeter: %f\n",
            eqTriangle.a, eqTriangle.b, eqTriangle.angle, eqTriangle.getArea(), eqTriangle.getPerimeter());
        System.out.printf("RightTriangle:\n\ta: %f, b: %f, angle: %f\n\tarea: %f\n\tperimeter: %f",
            rightTriangle.a, rightTriangle.b, rightTriangle.angle, rightTriangle.getArea(), rightTriangle.getPerimeter());
    }
    static double getSumArea(IsoscTriangle isoscTriangle, EqTriangle eqTriangle, RightTriangle rightTriangle) {
        return isoscTriangle.getArea() + eqTriangle.getArea() + rightTriangle.getArea();
    }
}
