#Primer creem l'usuari Mortadelo
New-ADUser -Name Mortadelo `
-SamAccountName Mortadelo `
-Enabled $true `
-Path “OU=PeppaCity,DC=nmasso,DC=cat" `
-AccountPassword (ConvertTo-SecureString “T1@_s3cr3t_S3rv1c3" -AsPlainText -Force) `
-PasswordNeverExpires $true `

#Modifiquem l'usuari ppony perque li caduqui el compte el 01/07/2022
Set-ADUser -Id ppony -AccountExpiration (Get-Date -Year 2022 -Month 7 -Day 1)

#l'afegim a la unitat personal P: a traves de DFS

#Modifiquem l'usari zzebra perque nome pugui iniciar sessio desde aquesta ordinador
Set-ADUser -Id zzebra 

#Fem l'script d'inici de sessió
New-Item -Name jugar.vbs `
-ItemType file `
-Path PRINCIPAL\PeppaEnterprise\scripts `
-Value msgbox"a plogut anem a jugar al jardí"

#Afegim l'script a zzebra
Set-ADUser -Id zzebra -ScriptPath jugar.vbs

#Creem els grup als que els afegirem
New-ADGroup -Name escola `
-GroupScope 1
New-ADGroup -Name amics `
-GroupScope 1

#afegim els usuaris a escola
Add-ADGroupMember -Identity “CN=escola,OU=PeppaCity,DC=nmasso,DC=cat” `
-Members “CN=Mortadelo,OU=PeppaCity,DC=nmasso,DC=cat”, “CN=zzebra,OU=PeppaCity,DC=nmasso,DC=cat”

Add-ADGroupMember -Identity “CN=amics,OU=PeppaCity,DC=nmasso,DC=cat” `
-Members “CN=ppony,OU=PeppaCity,DC=nmasso,DC=cat”, “CN=zzebra,OU=PeppaCity,DC=nmasso,DC=cat”
