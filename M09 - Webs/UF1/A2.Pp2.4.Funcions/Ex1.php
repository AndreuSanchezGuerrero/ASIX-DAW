<!-- Exercici 1. Si tenim dos variables (que, de moment les omplirem per codi) (1.5p).
	$a= 31
	$b= (Un altre valor enter)
Fes una funció que et demani quina operació vols fer (de moment el valor el posem per codi) i dins d’aquesta que hi hagi les cinc funcions necessàries per realitzar el que es demana a la llista

    1. La suma entre [valor a] i [valor b] és __.
    2. La resta entre [valor a] i [valor b] és __.
    3. El producte entre [valor a] i [valor b] és ___
    4. La divisió entre …
    5. El mòdul entre…-->
<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 1</h1>
        <title>Exercisi 1</title>
    </head>
    <body>
        <?php
            $a=31;
            $b=5;
            $operacio=1;
            function suma($a,$b){
                $suma=$a+$b;
                echo "La suma entre $a i $b és $suma";
            }
            function resta($a,$b){
                $resta=$a-$b;
                echo "La resta entre $a i $b és $resta";
            }
            function producte($a,$b){
                $producte=$a*$b;
                echo "El producte entre $a i $b és $producte";
            }
            function divisio($a,$b){
                $divisio=$a/$b;
                echo "La divisió entre $a i $b és $divisio";
            }
            function modul($a,$b){
                $modul=$a%$b;
                echo "El mòdul entre $a i $b és $modul";
            }
            function operacio($operacio,$a,$b){
                switch($operacio){
                    case 1:
                        suma($a,$b);
                        break;
                    case 2:
                        resta($a,$b);
                        break;
                    case 3:
                        producte($a,$b);
                        break;
                    case 4:
                        divisio($a,$b);
                        break;
                    case 5:
                        modul($a,$b);
                        break;
                }
            }
            operacio($operacio,$a,$b);
        ?>
        <a href="index.php" class="t"><button>Tornar</button></a>
    </body>
</html>
