: 'Apartat 1: Consulta d’instruccions. (1 punt)
1.1. Crea un usuari {on usuari@sapalomera.cat} (adduser / useradd). Serà [usuari2]
1.2. Justifica l’ús d’una instrucció o l’altra.

Apartat 2: Prioritats. (2 punts)
2.1 Obre un segon terminal, fes login amb l’[usuari2] i executa un procés infinit sense sortida per pantalla.
2.2 Torna al primer terminal, troba el procés anterior i posa’l com a menys prioritari.
2.3 Què identifica la columna tty? On trobes l’usuari?
2.4 Posa’l amb una prioritat de -25. Què passa? Per què? Posa’l amb una prioritat de -5.
2.5 Mata el procés infinit del segon terminal.

Apartat 3: Processos i treballs en segon pla. (4 punts)
3.1 Obre un segon terminal, fes login amb l’[usuari2] i executa un procés que duri 5000 segons.
Pots fer-ho amb el següent fitxer:
Has de donar-li permisos d’execució (chmod u+x 5000s.sh)
echo “hola”
date
sleep 5000
date
echo “acabat”

3.2 Troba el procés des del primer terminal.
3.3 Ves al segon terminal i posa el procés en segon pla. Comprova que el procés encara s’està executant. Si no s’està executant, que fes que ho faci, però en segon pla.
3.4 Obre un tercer terminal i executa un procés molt llarg (pots fer-ne servir un d’infinit). Compte, com que ja és tard, voldràs tancar el terminal per marxar (tanca’l), però el procés ha de seguir executant-se. Comprova-ho en el primer terminal.
3.5 Surt de la sessió del tercer terminal (els processos que quedin ja no estaran associats al terminal) i comprova des del primer terminal que encara tenim el procés infinit engegat. Finalitza’l.
3.6 Ves al segon terminal. Comprova les tasques que estan en segon pla.
3.7 Torna a posar la tasca 5000s.sh a primer pla i finalitza-la.
3.8 Executa altre cop la tasca ./5000s.sh, directament en segon pla, al tercer terminal.
3.9 Busca-la des del primer terminal amb l’ordre pstree (l’arbre de sistema és molt gran, hauràs de mirar només els processos de l’usuari). Pots trobar-lo? Per què?
3.10 Aconsegueix el pid del procés 5000s.sh, que estarà executant l’sleep 5000 i finalitza’l. Quines indicacions han aparegut al terminal 3? Tanca el terminal 3.
3.11 Vull mirar quina utilització dels recursos tinc, quina instrucció faig servir? Executa-la.
Quants usuaris tinc connectats? Quants processos s’estan executant? Pots marcar-ho a la pantalla.
Indica almenys una instrucció i el seu PID.
Amb la instrucció feta servir, només monitoritzes o pots executar instruccions? Posa un exemple.


Apartat # 4. Seqüència d’arrencada. (2,5 punts: 0,5+0,5+0,5+1)
# 4.1 A quina carpeta pots veure els dimonis que hi ha a l’ordinador?
# 4.2 Què són i per què serveixen les carpetes i els fitxers de /etc/rcN.d
# 4.3 Suposem que tenim un nivell d’execució (runlevel) 3, enumera la seqüència de carpetes i fitxers que s’executaran. En quines carpetes hi ha els scripts i les variables? Mostra un llistat de totes.
# 4.4 Obre un segon terminal. Al primer terminal, executa un shutdown.
A part del missatge un cop executat, comprova que tenim un shutdown pendent.
Cancel·la el shutdown. Comprova que ja no hi ha un shutdown pendent.
Quin paràmetre es necessita per a una aturada immediata?
Què ha passat (o hauria de passar) al segon terminal amb el shutdown i la cancel·lació?


Apartat 5. Documentació. (0,5 punts)
5.1 Realitza la documentació de tots els passos justificant les respostes.
5.2 Mostra les instruccions, els resultats i, si és el cas, la comprovació de l’execució, de forma que es vegi clarament quin punt s’està resolent i que les instruccions han fet el que s’esperava. Es valorarà la senzillesa de la solució.'





















# 1.1 Crea un usuari {on usuari@sapalomera.cat} (adduser / useradd). Serà [usuari2]
sudo adduser nmasso

# 1.2 Justifica l’ús d’una instrucció o l’altra.
# Utilitzarem un o altre en funció de les necessitats que tingui l'usuari. Si volem crear un usuari amb un home i un shell, utilitzarem adduser. Si volem crear un usuari sense home ni shell, utilitzarem useradd.

# 2.1 Obre un segon terminal, fes login amb l’[usuari2] i executa un procés infinit sense sortida per pantalla.
login nmasso
yes > /dev/null

# 2.2 Torna al primer terminal, troba el procés anterior i posa’l com a menys prioritari.
# Anem diretes als procesos de l'usuari
ps -u nmasso
sudo renice -20 1234

# 2.3 Què identifica la columna tty? On trobes l’usuari?
# tty identifica el terminal on s'està executant el procés
# l'usuari es troba a la columna USER, en el nostre cas no apareix ja q ja esteim selecionant un usuari concret

# 2.4 Posa’l amb una prioritat de -25. Què passa? Per què? Posa’l amb una prioritat de -5.
sudo renice -25 1234
# no es pot posar una prioritat inferior a -20 perque es el minim, per tant encara que posem -25, el procés seguirà tenint prioritat -20
sudo renice -5 1234

# 2.5 Mata el procés infinit del segon terminal.
kill 1234

# 3.1 Obre un segon terminal, fes login amb l’[usuari2] i executa un procés que duri 5000 segons.
login nmasso
nano 5000s.sh
chmod u+x 5000s.sh
./5000s.sh

# 3.2 Troba el procés des del primer terminal.
ps -u nmasso

# 3.3 Ves al segon terminal i posa el procés en segon pla. Comprova que el procés encara s’està executant. Si no s’està executant, que fes que ho faci, però en segon pla.
bg 1234
ps -u nmasso

# 3.5 Surt de la sessió del tercer terminal (els processos que quedin ja no estaran associats al terminal) i comprova des del primer terminal que encara tenim el procés infinit engegat. Finalitza’l.
exit
ps -u nmasso
kill 1234

# 3.6 Ves al segon terminal. Comprova les tasques que estan en segon pla.
jobs

# 3.7 Torna a posar la tasca 5000s.sh a primer pla i finalitza-la.
fg 1234
kill 1234

# 3.8 Executa altre cop la tasca ./5000s.sh, directament en segon pla, al tercer terminal.
./5000s.sh &
ps -u nmasso

# 3.9 Busca-la des del primer terminal amb l’ordre pstree (l’arbre de sistema és molt gran, hauràs de mirar només els processos de l’usuari). Pots trobar-lo? Per què?
pstree
# no es pot trobar perque no està associat a cap terminal

# 3.10 Aconsegueix el pid del procés 5000s.sh, que estarà executant l’sleep 5000 i finalitza’l. Quines indicacions han aparegut al terminal 3? Tanca el terminal 3.
ps -u nmasso
kill 1234
# no s'ha tancat el terminal 3 perque no està associat a cap terminal

# 3.11 Vull mirar quina utilització dels recursos tinc, quina instrucció faig servir? Executa-la. Quants usuaris tinc connectats? Quants processos s’estan executant? Pots marcar-ho a la pantalla. Indica almenys una instrucció i el seu PID. Amb la instrucció feta servir, només monitoritzes o pots executar instruccions? Posa un exemple.

# 4.1 A quina carpeta pots veure els dimonis que hi ha a l’ordinador?
# /etc/init.d
# 4.2 Què són i per què serveixen les carpetes i els fitxers de /etc/rcN.d
# /etc/rcN.d conté els enllaços simbòlics a /etc/init.d que s'executen en el nivell N
# 4.3 Suposem que tenim un nivell d’execució (runlevel) 3, enumera la seqüència de carpetes i fitxers que s’executaran. En quines carpetes hi ha els scripts i les variables? Mostra un llistat de totes.
# La sequencia de carpetes sera: /etc/rc3.d, /etc/rc2.d, /etc/rc1.d, /etc/rc0.d
# Estan a les carpetes /etc/rc3.d, /etc/rc2.d, /etc/rc1.d, /etc/rc0.d
# 4.4 Obre un segon terminal. Al primer terminal, executa un shutdown.
A part del missatge un cop executat, comprova que tenim un shutdown pendent.
Cancel·la el shutdown. Comprova que ja no hi ha un shutdown pendent.
Quin paràmetre es necessita per a una aturada immediata?
Què ha passat (o hauria de passar) al segon terminal amb el shutdown i la cancel·lació?

#cancelar un shutdown
sudo shutdown -c