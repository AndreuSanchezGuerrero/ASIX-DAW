#Creem els grups fifi, amigues, administradors de domini, dins de la OU Nintendo de nmasso.cat
New-ADGroup -Name "fifi" -GroupScope Global -Path "OU=Nintendo,DC=nmasso,DC=cat"
New-ADGroup -Name "amigues" -GroupScope Global -Path "OU=Nintendo,DC=nmasso,DC=cat"
New-ADGroup -Name "administradors de domini" -GroupScope Global -Path "OU=Nintendo,DC=namsso,DC=cat"

#Creem el nou User Pilaf a Users, resetejem la contrasenya a Rul3_th3_w0rld i el movem a la OU Nintendo de nmasso.cat
New-ADUser -Name "Pilaf" -Enabled $true -Path "CN=Users,DC=nmasso,DC=cat" -AccountPassword (ConvertTo-SecureString -String "Rul3_th3_w0rld" -AsPlainText -Force)
Move-ADObject -Identity "CN=Pilaf,CN=Users,DC=nmasso,DC=cat" -TargetPath "OU=Nintendo,DC=nmasso,DC=cat"

#Modifiquem l'user Daisy perque el compte li caduqui el 01/08/2022 
Set-ADAccountExpiration -Identity "Daisy" -DateTime "2022-08-0Global"

#Muntem al unitat personal S: a Daisy 
New-Item -Name UDaisy -Path \\PRINCIPAL\c$\Personals\
Set-ADUser -Identity "CN=Daisy,CN=Nintendo,DC=nmasso,DC=cat" -HomeDrive s: -HomeDirectory \\nmasso.cat\marioparty\UDaisy

#Afegim els Users Pilaf i Peach a el grup fifi
Add-ADGroupMember -Identity "CN=fifi,OU=Nintendo,DC=nmasso,DC=cat" -Member "CN=Pilaf,CN=Nintendo,DC=nmasso,DC=cat", "CN=Peach,CN=Nintendo,DC=nmasso,DC=cat" 

#Afegim l'user Pilaf al grup administradors de domini
Add-ADGroupMember -Identity "CN=administradors de domini,OU=Nintendo,DC=nmasso,DC=cat" -Member "CN=Pilaf,CN=Nintendo,DC=nmasso,DC=cat"

#Afegim els Users Peach i Daisy al grup amigues
Add-ADGroupMember -Identity "CN=amigues,OU=Nintendo,DC=nmasso,DC=cat" -Member "CN=Peach,OU=Nintendo,DC=nmasso,DC=cat", "CN=Daisy,CN=Nintendo,DC=nmasso,DC=cat"

#Creem l'script d'inici de sessio mush.vbs
New-Item -ItemType "file" -Name "mush.vbs" -Path "\\PRINCIPAL\c$\Personals\scripts" -Value "Mushroom kingdom!!"

#L'afegim a l'user Peach
Set-ADUser -Identity "CN=Peach,CN=Nintendo,DC=nmasso,DC=cat" -ScriptPath "\\PRINCIPAL\c$\Personals\scripts\mush.vbs"