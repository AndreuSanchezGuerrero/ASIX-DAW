

#Fem lo anterior pero utilitzant cat
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
            <h1>Exercici $i</h1>
            <title>Exercisi $i</title>
        </head>
        <body>
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
            <?php
            for (( i=1; i<=$exercisis; i++ ))
            do
                echo "<a href='Ex$i.php'>Exercici $i</a><br>";
            done
            ?>
        </body>
    </html>
EOF




