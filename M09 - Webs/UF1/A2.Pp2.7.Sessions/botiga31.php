<!-- Exercici 3 - La botiga a casa. Crea una pàgina web botigaXX.php que simuli una botiga online amb el típic carret de compra. Podrem afegir tants productes com vulguem (si el producte existeix, s’ha d’afegir la nova quantitat a la que ja teníem). És valorarà la utilització de funcions. (4.5p) -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 3</title>
    </head>
    <body>
        <h1>Exercici 3</h1>
        <h2>La botiga a casa</h2>
        <form action="botiga31.php" method="post">
            <p>Producte: <input type="text" name="producte"></p>
            <p>Quantitat: <input type="number" name="quantitat"></p>
            <input type="submit" name="afegir" value="Afegir a la cistella">
            <input type="submit" name="netejar" value="Netejar cistella">
        </form>
        <?php
            function afegir(){
                if (isset($_SESSION['cistella'])) {
                    $cistella = $_SESSION['cistella'];
                } else {
                    $cistella = array();
                }
                $producte = $_POST['producte'];
                $quantitat = $_POST['quantitat'];
                if (isset($cistella[$producte])) {
                    $cistella[$producte] += $quantitat;
                } else {
                    $cistella[$producte] = $quantitat;
                }
                $_SESSION['cistella'] = $cistella;
                $cistella = $_SESSION['cistella'];
                echo "<table border='1'>";
                echo "<tr><th>Producte</th><th>Quantitat</th></tr>";
                foreach ($cistella as $producte => $quantitat) {
                    echo "<tr><td>$producte</td><td>$quantitat</td></tr>";
                }
                echo "</table>";
            }
            session_start();
            if (isset($_POST['afegir'])) {
                afegir();
            }
            if (isset($_POST['netejar'])) {
                unset($_SESSION['cistella']);
            }
        ?>
    <a href="index.php"><button>Tornar</button></a>
    </body>
</html>
