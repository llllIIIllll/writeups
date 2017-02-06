package com.example.application;

import android.util.Base64;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.HashMap;
import java.util.Map;

public class Utilities {
    public static String doBoth(String input) {
        return translate(customEncodeValue(input));
    }

    public static String translate(String input) {
        int i;
        char[] inputchars = input.replace('=', '?').toCharArray();
        Map<Integer, Character> table = new HashMap();
        int[] numbers = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        char[] characters = new char[]{'W', 'h', 'a', 't', 'i', 's', 'd', 'o', 'n', 'e'};
        for (i = 0; i < 10; i++) {
            table.put(Integer.valueOf(numbers[i]), Character.valueOf(characters[i]));
        }
        for (i = 0; i < inputchars.length; i++) {
            int charcode = inputchars[i];
            if (charcode > 47 && charcode < 58) {
                inputchars[i] = ((Character) table.get(Integer.valueOf(charcode - 48))).charValue();
            }
        }
        return new String(inputchars);
    }

    public static String customEncodeValue(String input) {
        String output = "";
        byte[] input_bytes = input.getBytes();
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-224");
        } catch (NoSuchAlgorithmException e) {
        }
        md.update(input_bytes, 0, input_bytes.length);
        byte[] hash_bytes = md.digest();
        for (int i = 0; i < hash_bytes.length; i++) {
            output = output + String.format("%02x", new Object[]{Byte.valueOf(hash_bytes[i])});
        }
        return Base64.encodeToString(output.getBytes(), 0);
    }
}
