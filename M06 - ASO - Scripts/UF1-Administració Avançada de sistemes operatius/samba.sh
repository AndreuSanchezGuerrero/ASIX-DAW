Exercici 1: instal·lar i configurar el servei Samba.
Instal·la Samba en un servidor Linux en un entorn de xarxa igualitària.
El grup de treball s’anomenarà wg{cognom} > p.ex. wgjbasso
Com que és un servidor serà útil que el configuris amb una IP estàtica.

R1:
apt install samba
apt install smbclient

nano /etc/samba/smb.conf

[global]
workgroup = wgmasso

Exercici 2: creació i configuració de recursos.
Crea les carpetes i usuaris, que han de tenir aquests permisos:

uadmin
urrhh
/DirectoriCompartit


     /ccompartida
W uadmin
W urrhh
     /crrhhpublic
R uadmin
W urrhh
     /crrhh
- uadmin
W urrhh
     /cadmin
W uadmin
R urrhh

Afegeix una altra carpeta per l’usuari convidat. Amb quins permisos s’hi pot accedir?

R2:
mkdir /DirectoriCompartit
mkdir /DirectoriCompartit/ccompartida
mkdir /DirectoriCompartit/crrhhpublic
mkdir /DirectoriCompartit/crrhh
mkdir /DirectoriCompartit/cadmin
mkdir /DirectoriCompartit/cconvidat

smbpasswd -a uadmin
smbpasswd -a urrhh

nano /etc/samba/smb.conf
[DiretoriCompartit]
path = /DirectoriCompartit
valid users = uadmin, urrhh
browseable = yes

[DiretoriCompartit/ccompartida]
path = /DirectoriCompartit/ccompartida
valid users = uadmin, urrhh
write list = uadmin, urrhh

[DiretoriCompartit/crrhhpublic]
path = /DirectoriCompartit/crrhhpublic
valid users = uadmin, urrhh
read list = uadmin 
write list = urrhh

[DiretoriCompartit/crrhh]
path = /DirectoriCompartit/crrhh
valid users = urrhh
write list = urrhh

[DiretoriCompartit/cadmin]
path = /DirectoriCompartit/cadmin
valid users = uadmin urrhh
write list = uadmin
read list = urrhh

[DiretoriCompartit/cconvidat]
path = /DirectoriCompartit/cconvidat
guest ok = yes
guest only = yes
read only = no
writeable = yes

Canviem els permisiso a sambashare




systemctl restart smbd

Exercici 3: accés als recursos.
Realitza la configuració per tal d’accedir-hi des d’un client Linux i d’un Windows.
Recorda que tenim els permisos locals (servidor Linux) i de xarxa (Samba).
Per als permisos locals  chmod  però potser  ACL.

R3:
usermod -a -G uadmin urrhh
usermod -a -G urrhh uadmin

Exercici 4: permisos mitjançant grups.
Canvia la seguretat i, en comptes d’accedir amb usuaris, fes que s’accedeixi amb grups: gadmin i grrhh.
Afegeix 1 o 2 usuaris a cada grup i comprova que funciona.


Exercici 5: matrius de permisos.
De forma similar a l’exercici 2, fes una matriu de permisos que permeti oferir el servei per al següent escenari (calen tots els casos, però no cal indicar situacions repetides):
Suposem un centre escolar.
En el centre hi ha l’alumnat, el professorat, el personal d’administració i el de consergeria.
Per cada curs volem que l’alumnat pugui accedir a una carpeta on el professorat deixarà els documents amb teoria, exercicis, pràctiques o exàmens.
El professorat es divideix en departaments, p.ex. cicles, fol, matemàtiques, …
Cada departament tindrà una carpeta on el professorat podrà guardar els fitxers comuns.
Cada professor tindrà una carpeta d’ús personal que només podrà veure ell.
Administració tindrà una carpeta comuna i una per cadascun (com un dpt. de professors).
Hi haurà una carpeta per l’alumnat i una pel professorat on hi haurà documents públics que escriuran des d’administració i des de Direcció.
Direcció tindrà la consideració d’un altre departament de professorat.

R5:


Exercici 6: WSL.

https://learn.microsoft.com/en-us/windows/wsl/
https://learn.microsoft.com/es-es/windows/wsl/install

Fes una instal·lació de WSL.
    • Llegeix abans la documentació.
    • Compte amb la compatibilitat amb VmWare o VirtualBox.
    • Si per evitar problemes vols instal·lar-lo en una màquina virtual, mira si cal fer alguna cosa (habilitar virtualització aniuada).

Quins linux puc instal·lar?
     • Ubuntu
     • Debian
     • OpenSuse
     • Kali
     • Fedora
     • CentOS
     • Alpine
     • Arch
     • Gentoo
     • Pengwin


Com puc accedir als fitxers de Linux des del Windows? I al revés? amb WSL
Per ferho 

Quina utilitat li veus? En quins escenaris podria ser útil? Per producció?
La utilitat que li veig es que podria ser util per fer servir linux en un windows sense tenir que instal·lar linux en una maquina virtual. Per producció no ho veig util perque no es pot fer servir en producció.

Un escenari possible és el de tenir un servei (que tindrà poca càrrega) a fer servir des d’un navegador web (al windows). Identifica’n algun.
Un exeemple podria ser un servidor web que no tingui molta càrrega.









