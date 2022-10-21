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
            $decimal=31;
            function decimalABinari($decimal){
                $binari="";
                while ($decimal>0){
                    $binari=$binari.$decimal%2;
                    $decimal=$decimal/2;
                }
                echo "El nombre decimal $decimal en binari és $binari";
            }
            decimalABinari($decimal);
        ?>
    </body>
</html>
