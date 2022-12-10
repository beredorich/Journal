#Developer: Rich Beredo
#Purpose: parses text file to mark completed tasks
#Updated: 09DEC2022

$months = @('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
$monthNum = (Get-Date).Month
$currentMonth = $months[$monthNum-1]
$folderPath = Get-ChildItem -Path "C:\Users\richard.s.beredo\Journal" -Recurse | Where-Object {$_.Name -match $currentMonth} | ForEach-Object {$_.FullName}
write-host $folderPath
$files = Get-ChildItem -Path $folderPath -Recurse;

$i=0
foreach ($file in $files) {
    $i++;
    Write-Host "$i": $file.Basename;
}

$chosen = 69;
while ($chosen -ge $i+1){
    
    $chosen = Read-Host "Choose Week"
    if ($chosen -ge $i+1) {
        Write-Host "Invalid Input"
    }
}
$fileChosenPath = $folderPath + "\" + $files[$chosen-1]
Get-Content $fileChosenPath.Split('#') | Out-String