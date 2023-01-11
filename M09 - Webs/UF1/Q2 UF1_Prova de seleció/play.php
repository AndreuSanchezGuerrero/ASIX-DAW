<!--Demo de una app web que usa PHP per a practicar la taula del 6 i del 7.
Concideracions:
Tenim varis usuaris en banejats enmagatzemats en un .txt separats per;
Pagines a fer:
Pagina de conexio a la base de dades
Pagina de login per entrar a la app
Pagina amb la app  la cual nomes s'ha de poder entrar si l'usuari esta validat
Pagina amb el css


Fem el fitxer de joc: (Serveix pe l'susari practiqui la taula del 6 i del 7, el rang de la taula es de l'1 al 9)
1. Verifiquem la cookie per veure si l'usuari esta validat
    Si no ho esta, redirigeix a la pagina de login
    Si ho esta, mostra la app web 
2. Un cop verificat es genra la ronda:
    Te una durada de un minut
    Va genrant aletoriament operacions de la taula del 6 i del 7 q l'user ha de contestar
    Ha de habehi un contador amb les respostes correctes i un altre amb les respostes incorrectes a la part superior dreta de la pantalla
    Mostrem un contador amb el temps que queda per acabar la ronda
3. Cuan acaba la ronda:
    Rediriigeix a la pagina de app.php
    Calculem la puntuacio(encerts) de la ronda
    Afegim la puntuacio a la base de dades
    Mostrem la puntuacio de la ronda i la puntuacio record de l'usuari si aquesta es la record, ha d'estar actualitzada
    Mostrem un boto per anar a la taula global de records tornar a jugar o sortir de la app -->

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Juguem</title>
    </head>
    <body>
        <?php
            if (!isset($_COOKIE["usuari"]) || isset($_POST["logout"]) || $_COOKIE["usuari"] == "") {
                setcookie("usuari", "", time() - 3600);
                header("Location: index.php");
            }
            include "connectar.php";
            
            $usuari = $_COOKIE["usuari"];
            $encerts = 0;
            setcookie("temps", "temps", time() + 60);
            setcookie("encerts", $encerts, time() + 3600);
            #Mentre la cookie estigui activa, Genrem aleatoriament les operacions cada cop que s'encerta es carrega una de nova i s'anota un encert
            #Si la cookie no esta activa, es mostra la puntuacio de la ronda i la puntuacio record de l'usuari
            while (isset($_COOKIE["temps"])) {
                $operacio = rand(1, 2);
                $num1 = rand(6, 7);
                $num2 = rand(1, 9);
                if ($operacio == 1) {
                    $resposta = $num1 * $num2;
                    echo "$num1 * $num2 = ";
                } else {
                    $resposta = $num1 + $num2;
                    echo "$num1 + $num2 = ";
                }
                if (isset($_POST["resposta"])) {
                    if ($_POST["resposta"] == $resposta) {
                        $encerts++;
                        setcookie("encerts", $encerts, time() + 3600);
                    }
                }
            }
            $conn = connectar();
            $sql = "SELECT * FROM records WHERE usuari = '$usuari'";
            $result = $conn->query($sql);
            $row = $result->fetch();
            $record = $row["record"];
            $conn->close();
            if ($encerts > $record) {
                $conn = connectar();
                $sql = "UPDATE records SET record = '$encerts WHERE usuari = '$usuari'";
                $conn->query($sql);
                $conn->close();
            }
            echo "Puntuacio de la ronda: $encerts";
            echo "Puntuacio record: $record";
        ?>
        <form action="play.php" method="post">
            <input type="submit" name="logout" value="Sortir">
        </form>
    </body>
</html>