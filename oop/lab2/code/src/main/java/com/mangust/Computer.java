package com.mangust;

public class Computer {
  HardDrive hdd;
  String brand;
  int price;
  Computer(String brand, int price, int hddSizeMb) {
    this.brand = brand;
    this.price = price;
    this.hdd = new HardDrive(hddSizeMb);
  }
}
