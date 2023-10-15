package com.mangust;

public class EqTriangle extends Triangle {
    EqTriangle(double a, double b, double angle) {
        this.a = a;
        this.b = b;
        this.angle = angle;
    }

    @Override
    public double getArea() {
        return (Math.sqrt(3) * this.a * this.a) / 4;
    }

    @Override
    public double getPerimeter() {
        return 3 * this.a;
    }
}
