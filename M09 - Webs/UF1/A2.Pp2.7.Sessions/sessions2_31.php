<!-- Exercici 2 - Crea una altra pàgina que es dirà sessions2_XX.php. Amb aquesta pàgina has de permetre que es pugui consultar, modificar (si la variable de sessió existeix, actualitza el valor) o esborrar una variable de sessió, utilitza els recursos necessaris per poder-ho fer. És valorarà la utilització de funcions. (3.0p) -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 2</title>
    </head>
    <body>
        <h1>Exercici 2</h1>
        <form action="#" method="post">
            <label for="variable">Variable:</label>
            <input type="text" name="variable" id="variable">
            <label for="valor">Valor:</label>
            <input type="text" name="valor" id="valor">
            <input type="submit" value="Enviar" name="enviar">
            <input type="submit" value="Tancar sessió" name="tancar">
            <input type="submit" value="Consultar" name="consultar">
            <input type="submit" value="Modificar" name="modificar">
            <input type="submit" value="Esborrar" name="esborrar">  
        </form>
        <?php
        function crearSessio(){
            session_start();
            $_SESSION[$_POST['variable']] = $_POST['valor'];
            echo "Sessió: " . session_id() . "<br>";
            echo "Nom de la sessió: " . session_name() . "<br><br>";
            echo "Variables de sessió: " . "<br>";
            foreach ($_SESSION as $key => $value) {
                echo $key . " = " . $value . "<br>";
            }
        }
        function tancarSessio(){
            session_start();
            session_destroy();
            echo "Sessió tancada";
        }
        function consultarSessio(){
            session_start();
            echo "Sessió: " . session_id() . "<br>";
            echo "Nom de la sessió: " . session_name() . "<br><br>";
            echo "Variable de sessió consultada: " . "<br>";
            echo $_POST['variable'] . " = " . $_SESSION[$_POST['variable']] . "<br>";
        }
        function modificarSessio(){
            session_start();
            $_SESSION[$_POST['variable']] = $_POST['valor'];
            echo "Sessió: " . session_id() . "<br>";
            echo "Nom de la sessió: " . session_name() . "<br><br>";
            echo "Variable de sessió modificada: " . "<br>";
            echo $_POST['variable'] . " = " . $_SESSION[$_POST['variable']] . "<br>";
            $_SESSION[$_POST['variable']] = $_POST['valor'];
            echo "A canviat a:<br>";
            echo $_POST['variable'] . " = " . $_SESSION[$_POST['variable']] . "<br>";
        }
        function esborrarSessio(){
            session_start();
            echo "Sessió: " . session_id() . "<br>";
            echo "Nom de la sessió: " . session_name() . "<br><br>";
            echo "Variable de sessió eliminada: " . "<br>";
            echo $_POST['variable'] . " = " . $_SESSION[$_POST['variable']] . "<br>";
            #eliminem la variable de sessió
            unset($_SESSION[$_POST['variable']]);            
        }
        if (isset($_POST['enviar'])) {
            crearSessio();
        }
        if (isset($_POST['tancar'])) {
            tancarSessio();
        }
        if (isset($_POST['consultar'])) {
            consultarSessio();
        }
        if (isset($_POST['modificar'])) {
            modificarSessio();
        }
        if (isset($_POST['esborrar'])) {
            esborrarSessio();
        }
        ?>
    <a href="index.php"><button>Tornar</button></a>
    </body>
</html>
