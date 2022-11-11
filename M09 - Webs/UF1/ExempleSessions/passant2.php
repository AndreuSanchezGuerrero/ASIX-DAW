<!DOCTYPE html>
<html>
<head>
      <title>Sessions</title>
</head>
<body>
<?php

// Connectem amb la sessió
session_start();



echo "<h2>Passant valors de variable de sessió<br>";
echo "Fitxer actual: ".$_SERVER['PHP_SELF']."</h2><br>\n";

// Si la primera variable de sessió està definida...
if (isset($_SESSION['codi']))
{
    // Mostrem els valors de sessió que han arribat
    echo "<table>";
    echo "<tr><td> <b>Var. sessió codi:</b> </td><td>".$_SESSION['codi']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessió any:</b> </td><td>".$_SESSION['any']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessió pla:</b> </td><td>".$_SESSION['etapa']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessió curs:</b> </td><td>".$_SESSION['nivell']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessió grup:</b> </td><td>".$_SESSION['grup']."</td></tr>\n";
    echo "</table>";
}
else
{
    // Si la primera variable de sessió no està definida...
    // mostrem missatge 
    echo "Variables de sessió no definides \n";
}

echo "<br><br>Abans de seguir, la primera vegada aneu enrere amb el navegador per veure si es conserven els";
echo " valors de les variables de sessió tornat a la pàgina anterior";
echo "<br><br><a href=\"passant3.php?".session_name()."=".session_id();
echo "\">Segueix</a>";;



?>



</body>
</html>
