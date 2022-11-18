<!-- mplementa dues pantalles. A la primera hi ha d’haver quatre opcions (fes servir formulari de inputs de tipus radios button) que posteriorment podríem utilitzar per valorar exposicions (millorable, suficient, bé i molt bé). I a la segona s’ha de mostrar per pantalla els cops que s’ha escollit cada opció, també un botó o link per tornar a la pàgina del formulari i poder seguir valorant. (4.0p)-->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 1</title>
    </head>
    <body>
        <?php 
        $opcio = $_POST['opcio'];
        echo $opcio;
        if (isset($opcio)) {
            switch ($opcio) {
                case 'millorable':
                    if (isset($_COOKIE['millorable'])) {
                        $millorable = $_COOKIE['millorable'];
                        $millorable++;
                        setcookie('millorable', $millorable, time() + 3600);
                    } else {
                        setcookie('millorable', 1, time() + 3600);
                    }
                    break;
                case 'suficient':
                    if (isset($_COOKIE['suficient'])) {
                        $suficient = $_COOKIE['suficient'];
                        $suficient++;
                        setcookie('suficient', $suficient, time() + 3600);
                    } else {
                        setcookie('suficient', 1, time() + 3600);
                    }
                    break;
                case 'be':
                    if (isset($_COOKIE['be'])) {
                        $be = $_COOKIE['be'];
                        $be++;
                        setcookie('be', $be, time() + 3600);
                    } else {
                        setcookie('be', 1, time() + 3600);
                    }
                    break;
                case 'moltbe':
                    if (isset($_COOKIE['moltbe'])) {
                        $moltbe = $_COOKIE['moltbe'];
                        $moltbe++;
                        setcookie('moltbe', $moltbe, time() + 3600);
                    } else {
                        setcookie('moltbe', 1, time() + 3600);
                    }
                    break;
                }
            }
        #Si no s'ha escollit una opció, mostrem el formulari
        echo "Millorable: " . $_COOKIE['millorable'] . "<br>";
        echo "Suficient: " . $_COOKIE['suficient'] . "<br>";
        echo "Be: " . $_COOKIE['be'] . "<br>";
        echo "Molt be: " . $_COOKIE['moltbe'] . "<br>";       
        ?>
        <a href="Ex3.html"><button>Tornar</button></a>
    </body>
</html>
