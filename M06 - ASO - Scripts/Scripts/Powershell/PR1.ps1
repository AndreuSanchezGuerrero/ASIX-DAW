$MarquesCotxe = "Seat", "Renault", "Volkswaguen", "Citroën", "Opel", "Peugeot", "Fiat", "BMW", "Mercedes", "Škoda", "Mini", "Smart", "Alfa Romero", "Lancia", "Kia", "Hiundai", "Dacia", "Toyota", "Honda", "Misubishi", "Jeep", "Tesla" 

#Fem un menu per poder escollir quina opcio volem fer

$opcio = 0

while ($opcio -ne 7) {

    Write-Host "1. Fes un programa que llegeixi un número per teclat i mostri tots els números que hi ha des del 1 fins al número entrat per teclat, ambdós inclosos."

    Write-Host "2. Fes un programa que llegeixi un número (n), i mostri els n primers números parells"

    Write-Host "3. Fes un programa que mostri totes les marques de cotxes que comencin per S o comencin per T"

    Write-Host "4. Fes un programa que s’inventi un número del 1 al 100, i ens doni 7 intents per encertar-lo. Ens ha de dir cada vegada si el número inventat és major o menor que el entrat."

    Write-Host "5. Fes un programa que agafi cinc marques de cotxes a l’atzar i les mostri. Ha de ser les 5 diferents."

    Write-Host "6. Fes un programa per jugar al penjat amb powershell."

    $opcio = Read-Host "Escull una opcio"

    switch ($opcio) {
        1 {  
            $numero = Read-Host "Introdueix un numero"
            for ($i = 1; $i -le $numero; $i++) {
                Write-Host $i
            }
        }
        #Contem x numero de primers de 0 a infinit
        2 {  
            $numero = Read-Host "Introdueix un numero"
            $primers = 0
            $i = 1
            while ($primers -lt $numero) {
                $divisors = 0
                for ($j = 1; $j -le $i; $j++) {
                    if ($i % $j -eq 0) {
                        $divisors++
                    }
                }
                if ($divisors -eq 2) {
                    Write-Host $i
                    $primers++
                }
                $i++
            }
        }

        3 { 
            foreach ($cotxe in $MarquesCotxe) {
                if ($cotxe.Substring(0,1) -eq "S" -or $cotxe.Substring(0,1) -eq "T") {
                    Write-Host $cotxe
                }
            }
        }

        4 { 
            $numero = (Get-Random -Minimum 1 -Maximum 100)
            $intent = 0
            while ($intent -lt 7) {
                $numeroUsuari = Read-Host "Introdueix un numero"
                if ($numeroUsuari -eq $numero) {
                    Write-Host "Has encertat"
                    break
                } elseif ($numeroUsuari -gt $numero) {
                    Write-Host "El numero es mes petit"
                } else {
                    Write-Host "El numero es mes gran"
                }
                $intent++
            }
        }

        5 { 
            $cotxes = @()
            while ($cotxes.Count -lt 5) {
                
                $cotxe = $MarquesCotxe[(Get-Random -Minimum 0 -Maximum $MarquesCotxe.Count)]
                if ($cotxes -notcontains $cotxe) {
                    $cotxes += $cotxe
                }
            }
            foreach ($cotxe in $cotxes) {
                Write-Host $cotxe
            }
        }

        6 {
            #Fem un programa per jugar al pejat
            $paraula = Read-Host "Introdueix una paraula"
            $paraula = $paraula.ToUpper()
            $paraula = $paraula.ToCharArray()
            $paraulaMostrar = $paraula.Clone()
            for ($i = 0; $i -lt $paraulaMostrar.Length; $i++) {
                $paraulaMostrar[$i] = "_"
            }
            $intent = 0
            while ($intent -lt 7) {
                Write-Host "Intent: " $intent
                Write-Host $paraulaMostrar
                $lletra = Read-Host "Introdueix una lletra"
                $lletra = $lletra.ToUpper()
                $trobat = $false
                for ($i = 0; $i -lt $paraula.Length; $i++) {
                    if ($paraula[$i] -eq $lletra) {
                        $paraulaMostrar[$i] = $lletra
                        $trobat = $true
                    }
                }
                if ($trobat -eq $false) {
                    $intent++
                }
                if ($paraulaMostrar -eq $paraula) {
                    Write-Host "Has encertat la paraula"
                    break
                }
            }
            if ($intent -eq 7) {
                Write-Host "Has perdut"
            }
        }

        default { 
            Write-Host "Opcio incorrecta" 
        }
    }
    Read-Host "Prem una tecla per continuar"
}