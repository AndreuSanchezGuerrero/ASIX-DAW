<?php
    function connectar(){
        $servername = "localhost";
        $username = "user";
        $password = "aplicacions";
        $dbname = "meteo";
        try {
            $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $conn;
        } catch(PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
    }
    function tancar(){
        $conn = null;
    }
?>