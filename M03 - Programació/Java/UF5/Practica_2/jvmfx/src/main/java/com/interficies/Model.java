package com.interficies;

public class Model {
    // Decrementar el valor del comptador i mostrar-lo
    public static void decrementar() {
        int c = Integer.parseInt(Vista.getComptador());
        --c;
        Vista.setComptador("" + c);
    }

    // Incrementar el valor del comptador i mostrar-lo
    public static void incrementar() {
        int c = Integer.parseInt(Vista.getComptador());
        ++c;
        Vista.setComptador("" + c);
    }
}