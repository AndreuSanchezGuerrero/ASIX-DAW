echo "Quants exercisis vols generar?"
read exercisis
for (( i=1; i<=$exercisis; i++ ))
do
#Creem el fitxer
touch ./Ex$i.php
#Afegim el comentari
cat << EOF >> Ex$i.php
<!-- -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici $i</title>
    </head>
    <body>
        <h1>Exercici $i</h1>
        <?php
        
        ?>
    <a href="index.php"><button>Tornar</button></a>
    </body>
</html>
EOF
done

for (( i=1; i<=$exercisis; i++ ))
do
#Creem el fitxer
touch ./Ex$i.html
#Afegim el comentari
cat << EOF >> Ex$i.html
<!-- -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercici $i</title>
    </head>
    <body>
        <h1>Exercici $i</h1>
    <a href="index.php"><button>Tornar</button></a>
    </body>
</html>
EOF
done

#Fes una pagina php pamb botons que et permeti accedir a tots els exercisis generats
touch ./index.php
cat << EOF >> index.php
<!-- -->
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="CSS.css">
        <title>Exercicis</title>
        <h1>Exercicis</h1>
        <title>Exercisis</title>
    </head>
    <body>
EOF

for (( i=1; i<=$exercisis; i++ ))
do
cat << EOF >> index.php
        <a href="Ex$i.html"><button>Exercici $i</button></a>
EOF
done

cat << EOF >> index.php
    </body>
</html>
EOF
