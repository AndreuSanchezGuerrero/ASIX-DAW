<# Script per a configurar el DHCP amb PowerShell
L'àmbit s'ha de dir '1aConv-NMC'
Xarxa: 192.168.100.0/24
Rang DHCP: 20-88, inloses
DNS: 1.1.1.1
Lease: 2h 40min 
Reserva: 192.168.100.35 - AA:11:F1:BB:00:5E
#>
# Configuració de l'àmbit
$ambit = "1aConv-NMC"
$StartRange = "192.168.100.20"
$EndRange = "192.168.100.88"
$DNS = "1.1.1.1"
$Lease = "0.02:40:00"
$SubnetMask = "255.255.255.0"
$ReservaIP = "192.168.100.35"
$ReservaMAC = "AA:11:F1:BB:00:5E"
$ScopeId = "192.168.100.0"
# Creació de l'àmbit
Add-DhcpServerv4Scope -Name $ambit -StartRange $StartRange -EndRange $EndRange -SubnetMask $SubnetMask -LeaseDuration $Lease 
Set-DhcpServerv4OptionValue -ScopeId $ScopeId -Router 192.168.100.1 -DNSServer $DNS
Add-DhcpServerv4Reservation -ScopeId $ScopeId -IPAddress $ReservaIP -ClientId $ReservaMAC
#Mostrem tot lo q hem configurat
Get-DhcpServerv4Scope -ScopeId $ScopeId
Get-DhcpServerv4OptionValue -ScopeId $ScopeId -Router -DNSServer
Get-DhcpServerv4Reservation -ScopeId $ScopeId -IPAddress $ReservaIP -ClientId $ReservaMAC


