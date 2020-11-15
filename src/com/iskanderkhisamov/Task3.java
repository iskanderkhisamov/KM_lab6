package com.iskanderkhisamov;

import java.util.Random;

public class Task3 {

    public Task3() {
        System.out.println("\n\nЗадание 3\n");

        double x, y, hit;
        Random rnd = new Random();
        hit = 0;

        for (int i = 0; i < 200; i++) {
            x = rnd.nextDouble() * 10;
            y = rnd.nextDouble() * 16;
            if ((y - x * x <= 0) && (y + 4 * x < 40))
                hit++;
        }

        System.out.println("Площадь: " + (hit / 200) * 16 * 10);
    }
}
