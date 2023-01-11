Esteu fent pràctiques FCT en una empresa industrial.

El tutor de pràctiques us explica que aquesta empresa està organitzada en diferents departaments: administració, recursos humans, comercial, oficina tècnica, “supply chain management” (scm), producció, laboratori, qualitat,  expedicions, manteniment i informàtica.

Als departaments hi ha els següents usuaris:
- administració: Raymond Reddington (*), Elizabeth Keen, Donald Ressler; 
- recursos humans: Grace Musso (*);
- comercial: Richard Shrewsbury (*), Edmond Blackadder, Baldrick Dogsbody; 
- oficina tècnica: Johnny Fever, Bailey Quarters i Les Nessman; 
- “supply chain management”: Tim Taylor (*), Al Borland i Heidi Keppert; 
- producció: Willie Wonka (*), Charlie Bucket i Oompa Loompas (operaris); 
- laboratori: Walter White, Skyler White i Lydia Rodarte; 
- qualitat: Jane Marple i Hercule Poirot; 
- expedicions: Han Solo, Chewbacca Wookiee, Lando Calrissian; 
- manteniment: Rowan Bean; 
- informàtica: Roy Trenneman i Jen Barber. 
- A més els usuaris marcats amb (*) formen part de Direcció.

A nivell informàtic, tant els PCs de treball com els servidors són windows i estan configurats i treballant correctament. Hi ha diversos servidors, un dels quals fa de servidor de fitxers.

Cada usuari té un PC de treball assignat i, al servidor de fitxers, una carpeta personal on només hi pot escriure ell però tots els companys del departament poden veure’n el contingut. A més, tots els treballadors d’un departament tenen una carpeta amb documents de treball compartits.
Els usuaris de Direcció pertanyen a dos departaments: el seu i Direcció.
Els usuaris Oompa Loompas, els operaris de fàbrica (són diferents persones però es poden tractar com un sol usuari), són una excepció: poden entrar als diversos PCs que hi ha distribuïts per la fàbrica, però només poden accedir al servidor per veure els plànols de producció que fan a l’oficina tècnica. Hi ha una carpeta compartida (~d’oficines) per tots els usuaris excepte pels Oompa Loompas.

Finalment el tutor de pràctiques us ha deixat remenar els servidors. Tot xafardejant us adoneu que el servidor de fitxers està a punt de quedar ple. Això no pot ser i l’aviseu de seguida. Sap que el servidor de fitxers està al límit però el contracte de manteniment no finalitza fins d’aquí un any i no hi ha pressupost per comprar-ne un de nou amb les llicències de Windows.
Sabeu que té un servidor antic (hw) que no fa servir, coneixeu el Linux Ubuntu i algunes eines i, amb ganes d’ajudar, li demaneu poder fer una proposta / demostració per poder tenir un altre servidor de fitxers replicant l’esquema de l’existent. El tutor de pràctiques us ho accepta i us marca els següents punts que ha de tenir la proposta:

Com que es tracta d’un prototipus només es tindran en compte els usuaris d’oficina tècnica i de producció, ja que s’entén que contemplen tots els casos.


Apartat 1. Proposta tecnològica. (1p)
    • Explica què instal·laràs i amb quina configuració. Justifica la resposta.
[Un linux ub […] perquè [...]]


Apartat 2. Proposta d’organització. (1p)
    • Indica els grups, els usuaris, a quins grups pertany cada usuari, quines carpetes crearàs i quins permisos hi tindrà cada grup o usuari.
    • Et resultarà útil fer servir una matriu de permisos.
    • Nomenclatura: els grups començaran per ‘g’ i els usuaris per ‘u’ i en ambdós casos seguits per dues inicials vostres. Per exemple: gjbadmin o ujbamonk.


Apartat 3. Instal·lació de Samba i configuració. (3p)
    • Realitza (o readapta) i documenta el procés d’instal·lació i configuració de Samba.
    • Indica els noms, IPs o altres dades de configuració si les fas servir.


Apartat 4. Creació dels usuaris i grups. (1p)
    • Crea els usuaris i grups que has proposat a l’apartat 2.


Apartat 5. Creació de l’estructura de directoris i assignació de permisos. (1p)
    • Crea l’estructura de directoris i fes l’assignació de permisos indicats a l’apartat 2.


Apartat 6. Accés des d’un client windows comprovant els diferents permisos. (1p)
    • Indica les configuracions del windows que t’hagin fet falta.
    • Comprova els permisos d’accés, també quan no es té accés.

Apartat 7. Consultes vàries. (1,5p)
Veiem una part del contingut d’un fitxer de configuració.

[simpsons]
path = /DirectoriCompartit/CarpetaSimpsons
write list = homer, marge
read list = bart, lisa, maggie, @bouvier
create mask = 0775
directory mask = 0755

    1. A quin fitxer esperaries trobar aquest contingut (ruta completa)?

    2. Quan un usuari accedeixi des d’un client, amb quin nom veurà el recurs compartit?

    3. Quines comprovacions prèvies faries per assegurar que quan et vulguis connectar el primer cop des d’un client anirà bé?

    4. Els usuaris marge, patty i selma pertanyen a bouvier, què poden fer cadascuna (si només tenim en compte els permisos que veiem aquí)?

    5. Què fa l’apartat create mask? I el directory mask? Amb aquests valors, és necessari que apareguin?


Apartat 8. Documentació. (0,5p)
    • L’explicació del tutor de pràctiques us pot haver generat dubtes. Com que no està per aquí, podeu preguntar al tutor del centre.
    • Realitza la documentació de tots els passos. Cal fer-ho de forma ordenada i poder veure clarament quin punt s’està resolent. 
    • Mostra les instruccions, els resultats i, si és el cas, la comprovació de l’execució.
    • Es valorarà la senzillesa de la solució. El temps és limitat, la complicació excessiva penalitza.

Resolució:
A.1 Proposta
Instal·laré un linux ub amb samba perque és un sistema operatiu que permet compartir fitxers i que és molt senzill de configurar.

A.2 Organització
Grups:
    • Direcció: gnmdir
    • Producció: gnmprod
    • Oficina tècnica: gnmtec
    • Oompa Loompa: gnmoompa

Usuaris:
    Willie Wonka: unmwonka - gnmdir, gnmprod
    Charlie Bucket: unmchuck - gnmprod
    Oompa Loompa: unmoompa - gnmoompa
    Johnny Fever: unmfever - gnmtec
    Bailey Quarters: unmquart - gnmtec
    Les Nessman: unmnessm - gnmtec

Carpetes i permisos
/General 
    /Direcció gmdir:rw
        /DirPublic gnmdir:rw
    /Producció gnmprod:rw
        /ProdPublic gnmprod:rw
    /OficinaTècnica gnmtec:rw gnmoompa:r
        /Planols gnmtec:rw gnmoompa:r
        /TecPublic gnmtec:rw
    #Carpeta general compartit amb tothom excepte Oompa Loompa
    /Public gnmdir:rw gnmprod:rw gnmtec:rw 
    /Personals gnmdir:rw gnmprod:rw gnmtec:rw gnmoompa:rw

A.3 Instal·lació i configuració
    • Instal·lació de samba
        sudo apt-get install samba
    • Configuració de samba
        sudo nano /etc/samba/smb.conf
[General]
path = /General
write list = @gnmdir, @gnmprod, @gnmtec
read list = @gnmdir, @gnmprod, @gnmtec
create mask = 0775
directory mask = 0755

[Direcció]
path = /General/Direcció
write list = @gnmdir
read list = @gnmdir
create mask = 0775
directory mask = 0755

[Producció]
path = /General/Producció
write list = @gnmprod
read list = @gnmprod
create mask = 0775
directory mask = 0755

[OficinaTècnica]
path = /General/OficinaTècnica
write list = @gnmtec
read list = @gnmtec
create mask = 0775
directory mask = 0755

[Public]
path = /General/Public
write list = @gnmdir, @gnmprod, @gnmtec
read list = @gnmdir, @gnmprod, @gnmtec
create mask = 0775
directory mask = 0755

[Personals]
path = /General/Personals
write list = @gnmdir, @gnmprod, @gnmtec, @gnmoompa
read list = @gnmdir, @gnmprod, @gnmtec, @gnmoompa
create mask = 0775
directory mask = 0755

[Planols]
path = /General/OficinaTècnica/Planols
write list = @gnmtec
read list = @gnmtec, @gnmoompa
create mask = 0775
directory mask = 0755

[TecPublic]
path = /General/OficinaTècnica/TecPublic
write list = @gnmtec
read list = @gnmtec
create mask = 0775
directory mask = 0755

[DirPublic]
path = /General/Direcció/DirPublic
write list = @gnmdir
read list = @gnmdir
create mask = 0775
directory mask = 0755

[ProdPublic]
path = /General/Producció/ProdPublic
write list = @gnmprod
read list = @gnmprod
create mask = 0775
directory mask = 0755

    • Reiniciem el servei
        sudo service smbd restart
        
A.4 Creació d’usuaris i grups
• Creem els usuaris i els grups els usuaria
    sudo adduser unmwonka
    sudo adduser unmchuck
    sudo adduser unmoompa
    sudo adduser unmfever
    sudo adduser unmquart
    sudo adduser unmnessm
    sudo addgroup gnmdir
    sudo addgroup gnmprod
    sudo addgroup gnmtec
    sudo addgroup gnmoompa

• Afegim els usuaris als grups
    sudo adduser unmwonka gnmdir
    sudo adduser unmwonka gnmprod
    sudo adduser unmchuck gnmprod
    sudo adduser unmoompa gnmoompa
    sudo adduser unmfever gnmtec
    sudo adduser unmquart gnmtec
    sudo adduser unmnessm gnmtec

A.5 Creació de carpetes i assignació de permisos
    • Creem les carpetes
        sudo mkdir /General
        sudo mkdir /General/Direcció
        sudo mkdir /General/Producció
        sudo mkdir /General/OficinaTècnica
        sudo mkdir /General/Public
        sudo mkdir /General/Personals
        sudo mkdir /General/OficinaTècnica/Planols
        sudo mkdir /General/OficinaTècnica/TecPublic
        sudo mkdir /General/Direcció/DirPublic
        sudo mkdir /General/Producció/ProdPublic

    • Assignem els permisos
        sudo chown -R unmwonka:gnmdir /General/Direcció
        sudo chown -R unmchuck:gnmprod /General/Producció
        sudo chown -R unmfever:gnmtec /General/OficinaTècnica
        sudo chown -R unmfever:gnmtec /General/OficinaTècnica/Planols
        sudo chown -R unmfever:gnmtec /General/OficinaTècnica/TecPublic
        sudo chown -R unmwonka:gnmdir /General/Direcció/DirPublic
        sudo chown -R unmchuck:gnmprod /General/Producció/ProdPublic
        sudo chown -R unmwonka:gnmdir /General/Personals
        sudo chown -R unmwonka:gnmdir /General/Public

    • Assignem els permisos (Crec q es redundats si ja he oisat el parametre create mask)
        sudo chmod -R 0775 /General/Direcció
        sudo chmod -R 0775 /General/Producció
        sudo chmod -R 0775 /General/OficinaTècnica
        sudo chmod -R 0775 /General/Public
        sudo chmod -R 0775 /General/Personals
        sudo chmod -R 0775 /General/OficinaTècnica/Planols
        sudo chmod -R 0775 /General/OficinaTècnica/TecPublic
        sudo chmod -R 0775 /General/Direcció/DirPublic
        sudo chmod -R 0775 /General/Producció/ProdPublic

    • Reiniciem el servei
        sudo service smbd restart

A.6 Accés a les carpetes compartides
    • Accedim a les carpetes compartides
        //192.168.122.53

A.7 Consultes vàries. (1,5p)
Veiem una part del contingut d’un fitxer de configuració.

[simpsons]
path = /DirectoriCompartit/CarpetaSimpsons
write list = homer, marge
read list = bart, lisa, maggie, @bouvier
create mask = 0775
directory mask = 0755

    1. A quin fitxer esperaries trobar aquest contingut (ruta completa)?

    2. Quan un usuari accedeixi des d’un client, amb quin nom veurà el recurs compartit?

    3. Quines comprovacions prèvies faries per assegurar que quan et vulguis connectar el primer cop des d’un client anirà bé?

    4. Els usuaris marge, patty i selma pertanyen a bouvier, què poden fer cadascuna (si només tenim en compte els permisos que veiem aquí)?

    5. Què fa l’apartat create mask? I el directory mask? Amb aquests valors, és necessari que apareguin?

respostes:
1. /etc/samba/smb.conf
2. simpsons
3. Comprovar que el servei està actiu, que el fitxer de configuració està ben escrit, que els permisos dels fitxers i carpetes són els correctes, que els usuaris i grups estan creatsm que els usuaris pertanyen als grups correctes i que hi haigi una connexió a la xarxa entre el client i el servidor.
4. Patty i Selma poden llegir, marge pot llegir i escriure.
5. El create mask defineix els permisos que tindrà un fitxer quan es crea. El directory mask defineix els permisos que tindrà una carpeta quan es crea. No és necessari que apareguin ja que els valors per defecte són 0777 per als fitxers i 0755 per les carpetes.
