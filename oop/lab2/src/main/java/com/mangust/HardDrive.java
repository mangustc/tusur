package com.mangust;

class HardDrive {
    int sizeMb;

    HardDrive() {
        this(0);
    }

    HardDrive(int sizeMb) throws IllegalArgumentException {
        if (sizeMb < 0)
            throw new IllegalArgumentException(
                    "Hard drive size can't be lower than zero");
        this.sizeMb = sizeMb;
    }

    public int getSizeMb() {
        return sizeMb;
    }
}
