<!-- Dos jugadors automàtics jugant a cartes
1. Fase de preparació:
    1.1 Creem les baralles dels dos jugadors, cadascu tindra las seva propia baralla de poker la cual sera barrejada aletoriament, com a baralla de poker contindra els 4 pals amb les seves 14 cartes cadascun. 
        Hem de tenir en compte q el valor de la J sera 11, la Q sera 12 i la K sera 13 i l'as sera 14.
    1.2 Creem un algorisme q barregi cada baralla per separat.
2. Fase de joc:
    2.1 Cada juagador agafa dues cartes de la seva baralla i es comparen per determinar com a guanyador qui tingui la puntuacio mes alta.
    2.2 Cada jugador agafa 3 cartes de la seva baralla i es comparen per determinar com a guanyador qui tingui la puntuacio mes baixa.
    2.3 Cada jugador agafa 4 cartes de la seva baralla i es comparen per determinar com a guanyador qui tingui el major nombre de cartes iguals(amb el mateix valor)
3. Crear la partida:
    Creem la partida; creem les dos baralles, les barrejem i executem les tres fases del joc. Tot ha de ser automatic sense que el usuari hagi de fer res.
    Per establir el guanyador de la partida (el q tingui mes puntucio):
        Se li suma 3 punts al guanyador per cada fase que guanyi.
        El q guanyi la fase tambe se li suma el valor de la suma de les seves cartes i al perdedor 2/3 del valor de la suma de les seves cartes.
-->
<DOCTYPE html>
<html>
    <head>
        <meta charset=UTF-8>
        <link rel=stylesheet type=text/css href=CSS.css>
        <title>Cartes</title>
    </head>
    <body>
        <?php
        #Funcions:

        ##Creem les baralles dels jugadors:
        function creacioBaralles(){
            $baralla=array();
            $pals=array("P","C","T","D");
            $valors=array("2","3","4","5","6","7","8","9","10","11","12","13","14");
            foreach($pals as $pal){
                foreach($valors as $valor){
                    $baralla+=array($pal.$valor=>$valor);
                }
            }
            return $baralla;
        }

        ##Creem un algorisme q barregi cada baralla per separat sense fer us de la funcio shuffle.
        function barrejaBaralla($baralla){
            $barallaBarrejada=array();
            $numCartes=count($baralla);
            for($i=0;$i<$numCartes;$i++){
                $numAleatori=rand(0,count($baralla)-1);
                $barallaBarrejada[]=$baralla[$numAleatori];
                unset($baralla[$numAleatori]);
                $baralla=array_values($baralla);
            }
            return $barallaBarrejada;
        }

        function fase1(){
            global $barallaJ1, $barallaJ2, $puntuacioJ1, $puntuacioJ2;
            #Agafem dues cartes de cada baralla i sumem els valors de les cartes recordem q aquestes cartes queden eliminades de la baralla.    
            $Carta1_J1=array_shift($barallaJ1);
            $Carta2_J1=array_shift($barallaJ1);
            $Carta1_J2=array_shift($barallaJ2);
            $Carta2_J2=array_shift($barallaJ2);
            #Sumem els valors de les cartes:
            $ValorJ1 = intval(substr($Carta1_J1,0,-1)) + intval(substr($Carta2_J1,0,-1));
            $ValorJ2 = intval(substr($Carta1_J2,0,-1)) + intval(substr($Carta2_J2,0,-1));
            #Comprovem qui te la puntuacio mes alta:
            if($ValorJ1>$ValorJ2){
                $puntuacioJ1+=3+$ValorJ1;
                $puntuacioJ2+=2/3*$ValorJ2;
                echo "El jugador 1 ha guanyat la fase 1 amb una puntuacio de $ValorJ1 i el jugador 2 ha perdut amb una puntuacio de $ValorJ2";
            }else if($ValorJ1<$ValorJ2){
                $puntuacioJ2+=3+$ValorJ2;
                $puntuacioJ1+=2/3*$ValorJ1;
                echo "El jugador 2 ha guanyat la fase 1 amb una puntuacio de $ValorJ2 i el jugador 1 ha perdut amb una puntuacio de $ValorJ1";
            }else{
                echo "La fase 1 ha quedat empatada";
            }
        }

        function fase2(){
            global $barallaJ1, $barallaJ2, $puntuacioJ1, $puntuacioJ2;
            #Agafem tres cartes de cada baralla i sumem els valors de les cartes.    
            $Carta1_J1=array_shift($barallaJ1);
            $Carta2_J1=array_shift($barallaJ1);
            $Carta3_J1=array_shift($barallaJ1);
            $Carta1_J2=array_shift($barallaJ2);
            $Carta2_J2=array_shift($barallaJ2);
            $Carta3_J2=array_shift($barallaJ2);
            #Sumem els valors de les cartes:
            $ValorJ1 = intval(substr($Carta1_J1,0,-1)) + intval(substr($Carta2_J1,0,-1)) + intval(substr($Carta3_J1,0,-1));
            $ValorJ2 = intval(substr($Carta1_J2,0,-1)) + intval(substr($Carta2_J2,0,-1)) + intval(substr($Carta3_J2,0,-1));
            #Comprovem qui te la puntuacio mes alta:
            if($ValorJ1<$ValorJ2){
                $puntuacioJ1+=3+$ValorJ1;
                $puntuacioJ2+=2/3*$ValorJ2;
                echo "El jugador 1 ha guanyat la fase 2 amb una puntuacio de $ValorJ1 i el jugador 2 ha perdut amb una puntuacio de $ValorJ2";
            }else if($ValorJ1>$ValorJ2){
                $puntuacioJ2+=3+$ValorJ2;
                $puntuacioJ1+=2/3*$ValorJ1;
                echo "El jugador 2 ha guanyat la fase 2 amb una puntuacio de $ValorJ2 i el jugador 1 ha perdut amb una puntuacio de $ValorJ1";
            }else{
                echo "La fase 2 ha quedat empatada";
            }
        }

        function fase3(){

        }

        #Programa:
        ##Creem una baralla per a cada jugador:
        for($i=0;$i<2;$i++){
            $barallaJ[$i]=creacioBaralles();
            echo "Baralla del jugador $i: ";
            echo "$barallaJ[$i])";
        }
        ##Barregem cada baralla:
        for($i=0;$i<2;$i++){
            $barallaJ[$i]=barrejaBaralla($barallaJ[$i]);
        }
        echo "Les baralles dels jugadors s'han creat correctament";
        ##Creem un array per a cada jugador per a guardar la puntuacio de cada partida:
        for($i=0;$i<2;$i++){
            $PuntuacioJ[$i]=0;
        }
        ##Juguem:
        
        ?>
    </body>
</html>
