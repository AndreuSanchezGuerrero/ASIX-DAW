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
            <title>Exercisi $i</title>
        </head>
        <body>
            <h1>Exercici $i</h1>
            <?php
            
            ?>
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
            <a href="Ex$i.php"><button>Exercici $i</button></a>
EOF
done
#Afegim un boto per tornar a la pagina principal
cat << EOF >> index.php
        <a href="index.php"><button>Tornar</button></a>
        </body>
    </html>
EOF