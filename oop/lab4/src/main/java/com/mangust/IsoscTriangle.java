package com.mangust;

public class IsoscTriangle extends Triangle {
    IsoscTriangle(double a, double b, double angle) {
        this.a = a;
        this.b = b;
        this.angle = angle;
    }

    @Override
    public double getArea() {
        if (this.a == this.b)
            return (this.b * Math.sqrt(this.a * this.a - (this.b * this.b) / 4.0)) / 2.0;
        return (this.a * this.b * Math.sin(this.angle)) / 2.0;
    }

    @Override
    public double getPerimeter() {
        if (this.a == this.b)
            return (2.0 * this.a * Math.sin(this.angle)) + this.a + this.b;
        return this.a + this.b + Math.sqrt(this.a * this.a + this.b * this.b - 2 * this.a * this.b * Math.cos(angle));
    }
}
