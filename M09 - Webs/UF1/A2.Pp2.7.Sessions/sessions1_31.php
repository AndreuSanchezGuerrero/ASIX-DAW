<!-- Exercici 1 - Crea una pàgina que es digui sessions1_XX.php. Hi has de generar una sessió i ha de permetre-hi registrar variables. Per afegir els valors i les variables, crea dos caixes de text en un formulari, en una hi posaràs el nom de la variable i en l’altra el valor. 
    • Després de guardar la variable, fes que es mostri juntament amb l’identificador de sessió i el nom de la mateixa. 
    • També hi has d’afegir un botó que t’ha de permetre tancar la sessió (Comprova que quan tornes a generar una sessió l’identificador és que ens surt ja és diferent). Fes-ne una captura.
És valorarà la utilització de funcions. (2.0p) -->
<!DOCTYPE html>
<ht>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 1</title>
    </head>
    <bo>
        <h1>Exercici 1</h1>
        <form action="#" method="post">
            <label for="variable">Variable:</label>
            <input type="text" name="variable" id="variable">
            <label for="valor">Valor:</label>
            <input type="text" name="valor" id="valor">
            <input type="submit" value="Enviar" name="enviar">
            <input type="submit" value="Tancar sessió" name="tancar">
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

            if (isset($_POST['enviar'])) {
                crearSessio();
            }
            if (isset($_POST['tancar'])) {
                tancarSessio();
            }
        ?>
    <a href="index.php"><button>Tornar</button></a>
    </body>
</html>
