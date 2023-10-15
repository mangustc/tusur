package com.mangust;

import java.util.Stack;

public class Lab6 {
    public static void main(String[] args) {
        String in = "',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz";
        String out = "";

        System.out.println("In string: " + in);

        Stack<Character> sequence = new Stack<>();
        int sequenceLength = in.length();
        for (int i = 0; i < sequenceLength; i++)
            sequence.push(in.charAt(i));
        for (int i = 0; i < sequenceLength; i++)
            out += sequence.pop();

        System.out.println("Out string: " + out);
    }
}
