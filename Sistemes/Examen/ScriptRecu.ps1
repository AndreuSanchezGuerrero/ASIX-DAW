#Creem els grups fifi, amigues, administradors de domini, dins de la OU Nintendo de nmasso.cat
New-ADGroup -Name "fifi" -GroupScope Global -Path "OU=Nintendo,DC=nmasso,DC=cat"
New-ADGroup -Name "amigues" -GroupScope Global -Path "OU=Nintendo,DC=nmasso,DC=cat"
New-ADGroup -Name "administradors de domini" -GroupScope Global -Path "OU=Nintendo,DC=namsso,DC=cat"

#Creem el nou User Pilaf i el movem a la OU, resetejem la contrasenya a Rul3_th3_w0rld
New-ADUser -Name "Pilaf" -Enabled $true -Path "OU=Nintendo,DC=nmasso,DC=cat" -AccountPassword (ConvertTo-SecureString -String "Rul3_th3_w0rld" -AsPlainText -Force) 

#Modifiquem l'user Daisy perque el compte li caduqui el 0Global/08/2022 (altres opcions no fet)
Set-ADAccountExpiration -Identity "Daisy" -DateTime "2022-08-0Global"

#Afegim els Users Pilaf i Peach a el grup fifi
Add-ADGroupMember -Identity "CN=fifi,OU=Nintendo,DC=nmasso,DC=cat" -Member "CN=Pilaf,CN=Nintendo,DC=nmasso,DC=cat", "CN=Peach,CN=Nintendo,DC=nmasso,DC=cat" 

#Afegim l'user Pilaf al grup administradors de domini
Add-ADGroupMember -Identity "CN=administradors de domini,OU=Nintendo,DC=nmasso,DC=cat" -Member "CN=Pilaf,CN=Nintendo,DC=nmasso,DC=cat"

#Afegim els Users Peach i Daisy al grup amigues
Add-ADGroupMember -Identity "CN=amigues,OU=Nintendo,DC=nmasso,DC=cat" -Member "CN=Peach,CN=Nintendo,DC=nmasso,DC=cat", "CN=Daisy,CN=Nintendo,DC=nmasso,DC=cat"
