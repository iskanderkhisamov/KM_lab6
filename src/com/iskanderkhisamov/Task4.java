package com.iskanderkhisamov;

import java.util.Random;

public class Task4 {

    public Task4() {
        System.out.println("\nЗадание 4\n");

        double x, y, hit;
        Random rnd = new Random();
        hit = 0;

        for (int i = 0; i < 200; i++) {
            x = rnd.nextDouble() * 1;
            y = rnd.nextDouble() * 1;
            if ((y - (Math.sqrt(x * x + 1))) <= 0)
                hit++;
        }

        System.out.println("Площадь: " + (hit / 200) * Math.sqrt(2));
    }
}
