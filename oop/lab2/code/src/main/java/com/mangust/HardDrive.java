package com.mangust;

class HardDrive {
  int sizeMb;
  HardDrive() {
    this(0);
  }
  HardDrive(int sizeMb) {
    this.sizeMb = sizeMb;
  }

  public int getSizeMb() {
    return this.sizeMb;
  }
}
