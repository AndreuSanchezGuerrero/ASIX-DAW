<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
      <title>Sessions</title>
</head>
<body>
<?php

// Cada script que vulguem treballar amb la sessió activa
// ha d'incloure la funció session_start() al capdamunt
session_start();



// Recollim els valors transmesos pel formulari de l'array _POST
$codi = $_POST['codi'];
$any = $_POST['any'];
$etapa = $_POST['etapa'];
$nivell = $_POST['nivell'];
$grup = $_POST['grup'];

// Posem un títol
echo "<h2>Passant valors de variables de sessió<br>\n";
echo "Fitxer actual: ".$_SERVER['PHP_SELF']."</h2><br>\n";

// Mostrem les dades recollides: codi, any, etapa, nivell i grup
echo "<table>";
echo "<tr><td> <b>Var. sessió codi:</b> </td><td>".$codi."</td></tr>\n";
echo "<tr><td> <b>Var. sessió any:</b> </td><td>".$any."</td></tr>\n";
echo "<tr><td> <b>Var. sessió pla:</b> </td><td>".$etapa."</td></tr>\n";
echo "<tr><td> <b>Var. sessió curs:</b> </td><td>".$nivell."</td></tr>\n";
echo "<tr><td> <b>Var. sessió grup:</b> </td><td>".$grup."</td></tr>\n";
echo "</table>";

// Assignem els valors trobats a les variables de sessió, que es passaran
$_SESSION['any'] = $any;
$_SESSION['codi'] = $codi;
$_SESSION['etapa'] = $etapa;
$_SESSION['nivell'] = $nivell;
$_SESSION['grup'] = $grup;


// Establim link a pàgina següent. Li passem el nom de sessió
// i el seu identificador

echo "<br><br><a href=passant.php>Segueix</a>";


?>

</body>
</html>
