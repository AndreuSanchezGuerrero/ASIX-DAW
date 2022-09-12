#3A.
#Creem els grups, el grup administradors ja existeix
New-ADGroup -Name "Jedi" -GroupScope Global -Path "OU=StarWars,DC=nmasso,DC=cat"
New-ADGroup -Name "Pilot" -GroupScope Global -Path "OU=StarWars,DC=nmasso,DC=cat"
#Afegim els usaers als seus grups
Add-ADGroupMember -Identity Jedi -Member Luke,Leia
Add-ADGroupMember -Identity Pilot -Member Luke,Han
Add-ADGroupMember -Identity Administrator -Member Han
#Resetejem la contrasenya d'en Luke
Set-ADAccountPassword -Identity Luke `
-NewPassword (ConvertTo-SecureString “N0u_P@ss” -AsPlainText -Force) `
-OldPassword (ConvertTo-SecureString “Aa12345678” -AsPlainText -Force)
#Fem q Leia hagi de canviar la password el primer cop
Set-ADUser -Identity Luke `
-PasswordNeverExpires $false `
-ChangePasswordAtLogon $true
#Bloquejem el canvi de password de Han
Set-ADUser -Identity Han `
-CannotChangePassword $true
#Suposant q anira a la mateixa UnitatS q en luke simplement li afegim sino la hauriem de crear
Set-ADUser -Identity Leia -HomeDrive s: -HomeDirectory \\nmasso.cat\Falcon2\UnitatS
    #En cas q la haguesim de crear (potser shan de posar permisos)
    New-Item -Name <nomunitat> -Path \\nmasso.cat\Falcon2\
#Script d'inici de sessio
