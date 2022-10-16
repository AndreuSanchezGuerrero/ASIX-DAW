: 'Exercicis
    1. (cat+cut +sort). Mostrar els noms dels usuaris donats dalta en el sistema(fitxer passwd) i la seva shell dinici, ordenats alfabèticament i separant els dos camps per 4 guions.
    2. (cat+cut +sort).  Ídem anterior però que els separi per un tabulador i desi el resultat en el fitxer sortida1
    3. Ídem anterior,però que ordeni per la Shell, que ha de ser la segona columna
    4. (grep+wc). Quants usuaris tenen el seu directori personal a /home.
    5. (du+sort+tail). Nom del directori que més ocupa dintre de /usr, sense comptar /usr, només un nivel de profunditat
    6. (find). Tots els directoris on un usuari tingui permisos d’escritura dintre de /home. Hem d’indicar l’usuari
    7. (find+wc). Ídem anterior,però que compti els directoris.
    8. (find +wc). Total de fotos jpg dintre de /home
    9. (who+wc).Numero de sessions obertes al sistema
    10. (who+cut+sort+uniq+wc). Número d’usuaris distints connectats al sistema.
    11. (cat+cut+sort). Genera un nou fitxer amb els usuaris registrats al sistema ordenats alfabèticament.
    12. (find). Genera un fitxer amb els noms de tots els fitxers mp3 de /home que són propietat d’un usuari concret.
    13. Afegeix al fitxer  enexecucio.log el nom de tots els procesos que s’estant executant al sistema com a root.
    14. Ídem anterior però de l’usuari que executa l’script i que afegeixi a lesmevesexecucions.log. No facis servir la opció -u de ps, fes servir la variable d’entorn $USER
    15. Com podem saber quines són les variables d’entorn? Indica com accedir a alguna d’elles.
    16. (grep+tail+cut). Llista només el GID del dos últims grups del sistema que contenguin la letra “a”
    17. (ifconfig+grep). Fes un script que retorni la mac assignada a la tarja de xarxa que li passarem com a paràmetre. Per exemple si executem “./diguemMac.sh eth0”m’ha de dir la mac de eth0.
    18. (ping). Fes un Alies del ping perquè només faci 4 pings, anomena’l myping
    19. (ping+cut). Fes un script al que li passarem una adreça d’internet com a paràmetre, res de read, i li farà 4 pings, volem que només ens mostri el temps que ha trigat en fer cada ping.
Es pot fer servir el cut amb el –c? Raona la resposta'

#Exercici 1 
cat /etc/passwd | cut -d: -f1,7 --output-delimiter='----' | sort -t: -k1,1

#Exercici 2
cat /etc/passwd | cut -d: -f1,7 --output-delimiter='    '| sort -k1,1 > sortida1

#Exercici 3
cat /etc/passwd | cut -d: -f1,7 --output-delimiter='    '| sort -k2,2 > sortida2

#Exercici 4
cat /etc/passwd | grep "/home" | wc -l

#Exercici 5
du -s /usr/* | sort -n | tail -n 1

#Exercici 6
#Per a l'usuari utilitzare $USER
find /home -user $USER -perm -u=w

#Exercici 7
find /home -user $USER -perm -u=w | wc -l

#Exercici 8
find /home -name "*.jpg" | wc -l

#Exercici 9
who | wc -l

#Exercici 10
who | cut -d" " -f1 | sort | uniq | wc -l

#Exercici 11
cat /etc/passwd | cut -d: -f1 | sort > sortida3

#Exercici 12
find /home -user $USER -name "*.mp3" > sortida4

#Exercici 13
#Les separacions entre camps no son estandar per tant no sem acudeix com poder seleccionar nomes el valor name
ps -u root | cut -d" " -f(posició del valor name(en cas que fo exacta)) >> enexecucio.log

#Exercici 14
#No entenc com ferho sense el -u
ps -u $USER | cut -d" " -f(posició del valor name(en cas que fo exacta)) >> enexecucio.log

#Exercici 15
env
#Per accedir a una variable d'entorn utilitzarem $nom_variable

#Exercici 16
cat /etc/group | grep "a" | tail -n 2 | cut -d: -f3

#Exercici 17
./diguemMac.sh eth0

#Exercici 18
alias myping="ping -c 4"

#Exercici 19
./Ex19.sh
#Es pot fer servir el cut amb el –c? Raona la resposta'
#Si, la comanda seria:
#ping -c 4 $1 | cut -c 78- | grep "time"
