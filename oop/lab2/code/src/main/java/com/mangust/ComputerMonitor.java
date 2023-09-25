package com.mangust;

public class ComputerMonitor extends Computer {
  int monitorSize;
  ComputerMonitor(String brand, int price, int hddSizeMb, int monitorSize) {
    super(brand, price, hddSizeMb);
    this.monitorSize = monitorSize;
  }
  public void print() {
    System.out.println("ComputerMonitor:");
    System.out.println("\tbrand: " + this.brand);
    System.out.println("\tprice: " + this.price);
    System.out.println("\thddSizeMb: " + this.hdd.getSizeMb());
    System.out.println("\tmonitorSize: " + this.monitorSize);
  }
}
