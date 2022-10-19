<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 5</title>
        <h1>Exercici 5</h1>
    </head>
    <body>
        <?php
            #Fem una manera per a q l'usari seleccioni per pantalla la manera de generar la matriu
            echo "<form action=Ex5.php method=post>";
            echo "<input type=radio name=manera value=1>Manera 1";
            echo "<input type=radio name=manera value=2>Manera 2";
            echo "<input type=radio name=manera value=3>Manera 3";
            echo "<input type=submit value=Enviar>";
            echo "</form>";
            switch ($_POST["manera"]) {
                case 1:
                    $jugadors[0][0]=25;
                    $jugadors[0][1]=21;
                    $jugadors[0][2]=19;
                    $jugadors[0][3]=30;
                    $jugadors[0][4]=20;
                    $jugadors[1][0]=24;
                    $jugadors[1][1]=19;
                    $jugadors[1][2]=17;
                    $jugadors[1][3]=30;
                    $jugadors[1][4]=10;
                    $jugadors[2][0]=20;
                    $jugadors[2][1]=15;
                    $jugadors[2][2]=14;
                    $jugadors[2][3]=28;
                    $jugadors[2][4]=8;
                    break;
                case 2:
                    $jugadors = array(
                        "Grup A" => array(25, 21, 19, 30, 20),
                        "Grup B" => array(24, 19, 17, 30, 10),
                        "Grup C" => array(20, 15, 14, 28, 8)
                    );
                    break;
                case 3:
                    $jugadors = array(
                        "Grup A" => array("Escoleta" => 25, "Benjamín" => 21, "Aleví" => 19, "Infantil" => 30, "Juvenil" => 20),
                        "Grup B" => array("Escoleta" => 24, "Benjamín" => 19, "Aleví" => 17, "Infantil" => 30, "Juvenil" => 10),
                        "Grup C" => array("Escoleta" => 20, "Benjamín" => 15, "Aleví" => 14, "Infantil" => 28, "Juvenil" => 8)
                    );
                    break;
            }
            printr($jugadors);
        ?>
    </body>
</html>
