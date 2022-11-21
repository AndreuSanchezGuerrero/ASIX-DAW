'''
Exemple {usuari}: si l’usuari és n.masso “{usuari}” = "nmasso"


Apartat 1: instal·lar CUPS. (1p)
Instal·la CUPS al servidor. Un cop fet, indica i prova com es pot canviar el port del servei.

Apartat 2: afegir una impressora (1p)
Afegeix una impressora gerard{usuari} des de la línia de comandes i una impressora thio{usuari} des de l’entorn gràfic.

Apartat 3: mostrar les impressores (0,5p)
Mostra les impressores disponibles des de la línia de comandes.

Apartat 4: afegir una classe (0,5p)
Afegeix una classe sopa{usuari} des de la línia de comandes i afegeix-hi les dues impressores.

Apartat 5: afegir una classe (1p)
Instal·la la classe a un client Ubuntu i imprimeix un document de prova.

Apartat 6: desactivar una impressora (0,5p)
Desactiva la impresora thio{usuari} des de la línia de comandes.

Apartat 7: imprimir mitjançant la classe (1p)
Imprimeix un document a la classe sopa{usuari} i troba a quina impressora s’està imprimint. Pots canviar el document a l’altra impressora i com? Cancel·la la impressió per línia de comandes.

Apartat 8: impressora PDF (1p)
Instal·la una impressora PDF i imprimeix-hi el document a lliurar (o algun altre).

Apartat 9: documentació. (0,5 punts)
9.1 Realitza la documentació de tots els passos justificant les respostes.
9.2 Mostra les instruccions, els resultats i, si és el cas, la comprovació de l’execució, de forma que es vegi clarament quin punt s’està resolent i que les instruccions han fet el que s’esperava. Es valorarà la senzillesa de la solució.
'''

# 1. Instal·lar CUPS
sudo apt-get install cups
sudo apt-get install cups-client

# 1.1 Canviar el port del servei
sudo nano /etc/cups/cupsd.conf
# 1.2 Canviar el port del servei
sudo service cups restart

# 2. Afegeix una impressora gerard{usuari} des de la línia de comandes
lpadmin -p gerardnmasso -E -v socket:// 
# 2.1 Afegeix una impressora thio{usuari} des de l’entorn gràfic

# 3. Mostra les impressores disponibles des de la línia de comandes
lpstat -p

# 4. Afegeix una classe sopa{usuari} des de la línia de comandes
#creem la classe

lpadmin -p gerardnmasso -c sopanmasso 
lpadmin -p thionmasso -c sopanmasso

# 5. Instal·la la classe a un client Ubuntu i imprimeix un document de prova
sudo apt-get install cups-client
lpadmin -p sopamasso -E -v socket://192.168.100.100
lpstat -p

# 6. Desactiva la impresora thio{usuari} des de la línia de comandes
lpadmin -p thionmasso -u de

# 7. Imprimeix un document a la classe sopa{usuari} i troba a quina impressora s’està imprimint. Pots canviar el document a l’altra impressora i com? Cancel·la la impressió per línia de comandes
lp -d sopanmasso -o fit-to-page document.pdf
lpstat -o
# 7.1 Modificar el document a l’altra impressora

# 7.1 Cancel·la la impressió per línia de comandes
lpstat -o
lpstat -o -c 1
# 8. Instal·la una impressora PDF i imprimeix-hi el document a lliurar (o algun altre).
sudo apt-get install cups-pdf
lpstat -p
lp -d PDF -o fit-to-page document.pdf

