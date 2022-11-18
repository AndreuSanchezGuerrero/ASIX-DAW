<!-- Exercici 5. Logs. Estem programant la part de gestió de logs d'un mòdul. Hi ha previstos tres tipus de missatges: informació (info), avís (warning), error (error). La idea és facilitar mitjançant funcions la impressió d'aquests missatges. (2.5p).
Un exemple de sortida podria ser (fitxa’t amb els colors i mida dels caràcters):
[INFO] Servidor iniciat correctament. 
[INFO] Consum de cpu ok.
[WARNING] Consum de cpu elevat.
[ERROR] Missatge de correu retornat.
[INFO] Consum de cpu ok.
A més a més, volem definir mitjançant una variable global (que es diu nivellLog) el nivell de detall del log, o sigui, si volem que es mostrin tots els missatges o no. nivellLog ha de tenir un d'aquests valors: 
3: s'imprimeixen tots els tipus de missatges (info, warning i error)
2: s'imprimeixen només warning i error
1: s'imprimeixen només els missatges d’error
0: no s'imprimeix res. 
Programa les funcions adequades de manera que des de el nostre programa principal només haguem de fer:
warning("Consum de cpu elevat");
error("Missatge de correu retornat”);-->
<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Exercici 1</title>
        <h1>Exercici 5</h1>
        <title>Exercisi 5</title>
    </head>
    <body>
        <?php
            $nivellLog = 3;
            function info($missatge){
                global $nivellLog;
                if($nivellLog >= 3){
                    echo "<p class=info> [INFO] $missatge </p>";
                }
            }
            function warning($missatge){
                global $nivellLog;
                if($nivellLog >= 2){
                    echo "<p class=warning> [WARNING] $missatge </p>";
                }
            }
            function error($missatge){
                global $nivellLog;
                if($nivellLog >= 1){
                    echo "<p class=error> [ERROR] $missatge </p>";
                }
            }
            info("Servidor iniciat correctament.");
            info("Consum de cpu ok.");
            warning("Consum de cpu elevat.");
            error("Missatge de correu retornat.");
        ?>
        <a href="index.php" class="t"><button>Tornar</button></a>
    </body>
</html>
