<!DOCTYPE html>
<html>
<head>
      <title>Sessions</title>
</head>
<body>
<?php

// Connectem amb la sessi�
session_start();


echo "<h2>Passant valors de variable de sessi�<br>";
echo "Fitxer actual: ".$_SERVER['PHP_SELF']."</h2><br>\n";

// Si la primera variable de sessi� est� definida...
if (isset($_SESSION['codi']))
{
    // Mostrem els valors de sessi� que han arribat
    echo "<table>";
    echo "<tr><td> <b>Var. sessi� codi:</b> </td><td>".$_SESSION['codi']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessi� any:</b> </td><td>".$_SESSION['any']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessi� pla:</b> </td><td>".$_SESSION['etapa']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessi� curs:</b> </td><td>".$_SESSION['nivell']."</td></tr>\n";
    echo "<tr><td> <b>Var. sessi� grup:</b> </td><td>".$_SESSION['grup']."</td></tr>\n";
    echo "</table>";
}
else
{
    // Si la primera variable de sessi� no est� definida...
    // mostrem missatge 
    echo "Variables de sessi� no definides \n";
}

// Buidem el contingut de les variables de sessi�
session_unset();

echo "<br><br>Un cop vistos els valors de les variables, actualitzeu la p�gina i veureu";
echo " l'efecte de la funci� \"session_unset\"";


?>



</body>
</html>

