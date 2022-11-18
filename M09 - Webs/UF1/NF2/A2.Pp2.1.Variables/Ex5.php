<DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 5</title>
        <h1>Exercici 5</h1>
    </head>
    <body>
        <?php
        $nom="Nil";
        $cognom="Massó";
        $text="on estarà wally dins del text";
        $text=$nom." ".$cognom." ".$text;
        echo "La llargada de l'String resulant és ".strlen($text).".<br>";
        echo "La posició de Wally és ".strpos($text,"wally").".<br>";
        ?>
    </body>