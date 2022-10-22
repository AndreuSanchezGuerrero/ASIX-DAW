<!-- Exercici 4. Crea una funció que converteixi nombres en base decimal a binaris (en forma d’String). El nombre decimal a treballar el tindrem com a variable al codi. S’ha de resoldre amb el màxim de funcions possible que “ajudin ” a la funció principal. A la imatge es mostra com passar de decimal a binari. (2.5p)-->
<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 4</h1>
        <title>Exercisi 4</title>
    </head>
    <body>
        <?php
            function decimalABinari($decimal){
                $binari = "";
                while($decimal > 0){
                    $binari = $decimal % 2 . $binari;
                    $decimal = floor($decimal / 2);
                }
                echo "El número binari és: " . $binari;
            }
            $decimal = 31;
            echo decimalABinari($decimal);
        ?>
        <a href="index.php" class="t"><button>Tornar</button></a>
    </body>
</html>
