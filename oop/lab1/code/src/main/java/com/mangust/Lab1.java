package com.mangust;

import java.util.Scanner;

public class Lab1 {
    public static void main(String[] args) {
        System.out.print("Enter a 6-digit number: ");
        String userStr = getString();

        int firstHalf = getSumByStrIndex(userStr, 0, 2);
        int secondHalf = getSumByStrIndex(userStr, 3, 5);

        if (isLuckyTicket(firstHalf, secondHalf))
            System.out.println("This is a lucky ticket!");
        else
            System.out.println("This is not a lucky ticket!");

        return;
    }

    public static boolean isLuckyTicket(int firstHalf, int secondHalf) {
        if (firstHalf % 2 != 0 || secondHalf % 2 != 0)
            return false;
        if (firstHalf == secondHalf)
            return true;
        return false;
    }

    public static int getSumByStrIndex(String numStr, int startIndex, int endIndex) {
        int sum = 0;

        for (int i = startIndex; i <= endIndex; i++)
            sum += Character.getNumericValue(numStr.charAt(i));

        return sum;
    }

    public static String getString() {
        Scanner userInput = new Scanner(System.in);
        String userString = userInput.nextLine();
        userInput.close();
        return userString;
    }

}
