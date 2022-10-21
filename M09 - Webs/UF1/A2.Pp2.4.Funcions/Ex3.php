<!-- Exercici 3. Suma Programa una funció "suma" que sumi tots els valors que li passem com a paràmetres. Els paràmetres poden ser variables i com a mínim se n’ha de passar un. Si cridem a la funció sense arguments ha de mostrar un missatge de error (de tipus ERROR de l’exercici anterior). La sortida també ha d'indicar el nombre de paràmetres que s'han sumat. (1.5p).
Exemple de sortida:
5+10+5+8+2+4+6+5 = 45.
Total operands sumats: 8-->
<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 3</h1>
        <title>Exercisi 3</title>
    </head>
    <body>
        <?php
            function suma(){
                $suma=0;
                $num_args = func_num_args();
                $sortida = "";
                if ($num_args==0){
                    echo "ERROR";
                }else{
                    for ($i=0;$i<$num_args;$i++){
                        while ($i <= $num_args-1){
                            $sortida .= func_get_arg($i) . " + ";
                        }
                        $suma = $suma+func_get_arg($i);
                    }
                    echo "La suma de $sortida és $suma<br>";
                    echo "La suma és $suma";
                }
            }
            suma(5,10,5,8,2,4,6,5);
        ?>
        <a href="index.php" class="t"><button>Tornar</button></a>
    </body>
</html>
