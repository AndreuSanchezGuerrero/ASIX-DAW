package com.interficies;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Button;

public class Controlador implements EventHandler<ActionEvent> {

    @Override
    public void handle(ActionEvent event) {
        // Modificar el comptador
        if (event.getSource() instanceof Button) {
            Button button = (Button) event.getSource();
            // Aixo es podria der millor per a que si es canvia el nom dels botons no doni problemes
            if (button.getText().equals("Dec")) {
                Model.decrementar();
            } else if (button.getText().equals("Inc")) {
                Model.incrementar();
            }
        }
    }
}