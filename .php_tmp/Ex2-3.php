<!--Exercici 1: (1.0p) Crea una base de dades per tal de poder “guardar” les dades que obtenim de les incidències que hem treballant en una activitat anterior. ALERTA amb els valors amb els que l’has de crear: (El servidor localhost, el nom de la BDD ha de ser incidencies, l’usuari user i el password aplicacions. (Recorda que es necessari l’script generat afegit a l’entrega)
-->
<!--Exercici 2 – Canvia la pàgina del formulari que es fa implementar en l’activitat corresponent per tal de poder afegir incidències a aquesta bases de dades. Decideix tu com a analista programador de l’aplicació com decidim si una incidència ja està entrada a la base de dades, si això passa no s’hi afegirà, es valorarà com aquest fet s’adverteix-hi a l’usuari així com la imprescindible utilització de funcions (s’ha de fer servir un fitxer de connexió tal i com es mostra a les captures). (6.5p)
-->  
<!--Exercici 3 – Afegeixi a l’anterior exercici un botó que quan el cliquem ens mostri totes les incidències que tenim a al base de dades, es valorarà la presentació de les mateixes així com la imprescindible utilització de funcions. (2.5p)
--> 
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici 2-3</title>
    </head>
    <body>
        <h1>Exercici 2-3</h1>
        <?php 
        #Fem uns funcio per a obrir i tancar la connexió a la base de dades
        function connectar(){
            $conn = mysqli_connect("192.168.122.59","usuari","aplicacions","incidencies");
            if (!$conn) {
                die("Connection failed: " . mysqli_connect_error());
            } else {
                echo "Connected successfully";
                return $conn;
            }
        }
        function tancar($conn){
            mysqli_close($conn);
        }
        #Fem una funció per a comprovar si l'incidencia ja existeix
        function comprovar($id){
            $conn = connectar();
            $sql = "SELECT * FROM incidencies WHERE id = '$id'";
            $result = mysqli_query($conn, $sql);
            if (mysqli_num_rows($result) > 0) {
                return true;
            } else {
                return false;
            }
            tancar($conn);
        }
        #Fem una funció per a afegir una incidencia a la base de dades
        function afegir($id, $dispositiu, $data, $solicitat, $correu, $descripcio){
            $conn = connectar();
            $sql = "INSERT INTO incidencies (id, dispositiu, data, solicitat, correu, descripcio) VALUES ('$id', '$dispositiu', '$data', '$solicitat', '$correu', '$descripcio')";
            if (mysqli_query($conn, $sql)) {
                echo "Incidencia afegida correctament";
            } else {
                echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }
            tancar($conn);
        }
        #Fem una funció per a mostrar totes les incidencies
        function mostrar(){
            $conn = connectar();
            $sql = "SELECT * FROM incidencies";
            $result = mysqli_query($conn, $sql);
            if (mysqli_num_rows($result) > 0) {
                echo "<table><tr><th>ID</th><th>Dispositiu</th><th>Data</th><th>Solicitat</th><th>Correu</th><th>Descripció</th></tr>";
                while($row = mysqli_fetch_assoc($result )) {
                    echo "<tr><td>".$row["id"]."</td><td>".$row["dispositiu"]."</td><td>".$row["data"]."</td><td>".$row["solicitat"]."</td><td>".$row["correu"]."</td><td>".$row["descripcio"]."</td></tr>";
                }
                echo "</table>";
            } else {
                echo "0 results";
            }
            tancar($conn);
        }

        #Comprovem si s'ha fet click al botó d'afegir o al de mostrar
        if(isset($_POST['enviar'])){
            $id = $_POST['id'];
            $dispositiu = $_POST['dispositiu'];
            $data = $_POST['data'];
            $solicitat = $_POST['solicitat'];
            $correu = $_POST['correu'];
            $descripcio = $_POST['descripcio'];
            if(comprovar($id)){
                echo "L'incidencia ja existeix";
            }else{
                echo "L'incidencia s'ha afegit correctament";
                afegir($id, $dispositiu, $data, $solicitat, $correu, $descripcio);
            }
            echo "<a href='Ex2.html'>Tornar</a>";
        }
        echo "Les incidencies són:";
        mostrar();
        echo "<a href='Ex2.html'>Tornar</a>";
        ?>
        <a href="Ex2.html" class="t"><button>Tornar</button></a>
    </body>
</html>




