# Windows Script to change the background of the desktop to an image named as the month from a directory

# Get the current month
$month = (Get-Date).ToString("MMMM")
#print the month
Write-Host $month

# Get the path to the image
$monthImage = "C:\Users\Adriana\Pictures\Backgrounds\" + $month + ".png"

# Set the background
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value $monthImage

# Refresh the desktop
Rundll32.exe user32.dll,UpdatePerUserSystemParameters

# Refresh the explorer



