package com.mangust;

public class RightTriangle extends Triangle {
    RightTriangle(double a, double b, double angle) {
        this.a = a;
        this.b = b;
        this.angle = angle;
    }

    @Override
    public double getArea() {
        if (this.angle == 90.0)
            return (this.a * this.b) / 2.0;
        if (this.a > this.b)
            return (this.a * this.a * Math.cos(this.angle * Math.PI / 180.0)) / 2.0;
        return (this.b * this.b * Math.cos(this.angle * Math.PI / 180.0)) / 2.0;

    }

    @Override
    public double getPerimeter() {
        if (this.angle == 90.0)
            return this.a + this.b + Math.sqrt(this.a * this.a + this.b * this.b);
        if (this.a > this.b)
            return this.a * (Math.cos(this.angle * Math.PI) / 180.0 + 1) + this.b;
        return this.b * (Math.cos(this.angle * Math.PI) / 180.0 + 1) + this.a;
    }
}

