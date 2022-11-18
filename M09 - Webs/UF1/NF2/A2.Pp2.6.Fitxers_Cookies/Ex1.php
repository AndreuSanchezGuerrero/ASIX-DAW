<!-- Crea una plana web d’accés, hi ha d’haver un formulari on poder-hi afegir usuaris (si no estem entrats) o accedir-hi directament demanant l’usuari i la contrasenya. Els usuaris han d’estar guardats en un fitxer usuarisXX.txt amb el següent format:
usuari1=password1
usuari2=password2
...
Finalment si és el primer cop que entrem a la pàgina en els darrers 30 segons ens ha de donar la benvinguda i que ens digui ben tornats altrament... És valorarà la utilització de funcions i arrays en la resolució de l’exercici així com la utilització d’estils en arxiu CSS. (2.5p).-->
<!--     <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" type="text/css" href="CSS.css">
            <title>Exercici 1</title>
        </head>
        <body>
            <h1>Exercici 1</h1>
            <form action="Ex1.php" method="post">
                <label for="user">Usuari:</label>
                <input type="text" name="user" id="user" required>
                <label for="password">Contrasenya:</label>
                <input type="password" name="password" id="password" required>
                <input type="radio" name="action" value="login" id="login" checked>
                <label for="login">Accedir</label>
                <input type="radio" name="action" value="register" id="register">
                <label for="register">Registrar-se</label>
                <input type="submit" value="Enviar">
            <a href="index.php"><button>Tornar</button></a>
        </body>
    </html>
-->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 1</title>
    </head>
    <body>
        <?php
            $user = $_POST['user'];
            $password = $_POST['password'];
            $action = $_POST['action'];
            $file = fopen("usuaris31.txt", "r");
            $users = array();
            $passwords = array();
            $i = 0;
            while(!feof($file)){
                $line = fgets($file);
                $users[$i] = substr($line, 0, strpos($line, "="));
                $passwords[$i] = substr($line, strpos($line, "=") + 1, strlen($line));
                $i++;
            }
            fclose($file);
            if($action == "login"){
                if(in_array($user, $users)){
                    $index = array_search($user, $users);
                    if($passwords[$index] == $password){
                        if (isset($_COOKIE['lastLogin'])) {
                            echo "Ben tornat!";
                        } else {
                            echo "Benvingut";
                        }
                        setcookie("lastLogin", time(), time() + 30);
                    }else{
                        echo "Contrasenya incorrecta";
                    }
                }else{
                    echo "Usuari no registrat";
                }
            }else if($action == "register"){
                if(in_array($user, $users)){
                    echo "Usuari ja registrat";
                }else{
                    $file = fopen("usuaris31.txt", "a");
                    fwrite($file, "$user=$password");
                    fclose($file);
                    echo "Usuari registrat";
                }
            }else{
                # print de totes les variables
                echo "user: $user<br>";
                echo "password: $password<br>";
                echo "action: $action<br>";
                echo "file: $file<br>";
                echo "users: $users<br>";
                echo "passwords: $passwords<br>";
                echo "i: $i<br>";
                echo "Error";
            }
        ?>
        <a href="index.php"><button>Tornar</button></a>
    </body>
</html>
