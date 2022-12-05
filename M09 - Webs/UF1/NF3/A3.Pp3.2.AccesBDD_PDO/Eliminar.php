<?php
    include 'Connectar.php';
    #Eliminem la incidencia i tornem a la pagina anterior
    #no cal comprovar si la incidencia existeix ja que si a la pagina anterior apareix el boto de eliminar es que existeix
    #no cal mostrar missatge de que s'ha eliminat correctament ja que si no apareix a la pagina de mostrar es que s'ha eliminat correctament
    $id = $_GET['id'];
    $conn = connectar();
    $sql = "DELETE FROM incidencies WHERE id = $id";
    $conn->exec($sql);
    tancar($conn);
    header("Location: Mostrar.php");
?>