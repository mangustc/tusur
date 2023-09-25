package com.mangust;

public class Lab2 {
  public static void main(String[] args) {
    Computer pc = new Computer("brand", 10000, 100000);
    System.out.println(pc.brand);

    ComputerMonitor pcMonitor = new ComputerMonitor("brand", 10000, 100000, 10);
    pcMonitor.print();
  }
}
