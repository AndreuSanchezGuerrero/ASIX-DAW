package com.interficies;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

public class Vista extends Application {

    private static TextField comptador;
    public static Object dButton;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) {
        BorderPane root = new BorderPane();
        Scene scene = new Scene(root, 300, 100);

        // Barra de menú
        MenuBar menuBar = new MenuBar();
        Menu menu = new Menu("Menu");
        MenuItem exitItem = new MenuItem("Tancar");
        exitItem.setOnAction(e -> stage.close());
        menu.getItems().addAll(exitItem);
        menuBar.getMenus().addAll(menu);
        root.setTop(menuBar);

        // Etiqueta on escriure el valor del comptador
        comptador = new TextField();
        comptador.setPrefWidth(100);
        comptador.setAlignment(Pos.CENTER);
        comptador.setEditable(false);

        // Botons per incrementar/decrementar el comptador i controlador
        Button dButton = new Button("Dec");
        Button iButton = new Button("Inc");
        Controlador ctrl = new Controlador();
        dButton.setOnAction(ctrl);
        iButton.setOnAction(ctrl);

        // Posar els botons en un HBox
        HBox buttons = new HBox();
        buttons.setSpacing(10);
        buttons.setPadding(new Insets(10, 10, 10, 10));
        buttons.getChildren().addAll(dButton, iButton);

        
        root.setCenter(comptador);
        root.setBottom(buttons);

        stage.setScene(scene);
        stage.show();

        // Set the comptador text
        Vista.setComptador("0");
    }

    // Actualitzar el comptador
    public static String getComptador() {
        return comptador.getText();
    }

    // Actualitzar el comptador
    public static void setComptador(String c) {
        comptador.setText(c);
    }

}