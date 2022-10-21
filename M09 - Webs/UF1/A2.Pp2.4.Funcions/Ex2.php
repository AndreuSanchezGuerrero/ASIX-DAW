<!-- Exercici 2. Primers Volem saber els números primers que hi ha entre dos valors. (1.5p).
Dissenya dues funcions:
    • Funció EsPrimer que donat un numero passat per paràmetre em retornarà si un número és primer o no (cert o fals)
    • Funcio PrimersValors que, donats dos números, m’imprimeixi els números que són primers. Aquesta funció no retornarà res.
Per provar-ho des del programa principal feu tres crides a PrimersValors, amb els valors (2 i 8), (3 i 29) i (30, 125).-->
<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 2</h1>
        <title>Exercisi 2</title>
    </head>
    <body>
        <?php
            function EsPrimer($num){
                $esPrimer=true;
                for($i=2;$i<$num;$i++){
                    if($num%$i==0){
                        $esPrimer=false;
                    }
                }
                return $esPrimer;
            }
            function PrimersValors($num1,$num2){
                for($i=$num1;$i<=$num2;$i++){
                    if(EsPrimer($i)){
                        echo "$i ";
                    }
                }
            }
            PrimersValors(2,8);
            echo "<br>";
            PrimersValors(3,29);
            echo "<br>";
            PrimersValors(30,125);
        ?>
    </body>
</html>
