<?php
    #Fem uns funcio per a obrir i tancar la connexió a la base de dades
    function connectar(){
        #Variables de connexió
        $servername = "192.168.122.59";
        $username = "perepi";
        $password = "pastanaga";
        $dbname = "aplicacio";
        try {
            $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $conn;
        } catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }
    function tancar($conn){
        $conn = null;
    }
?>
