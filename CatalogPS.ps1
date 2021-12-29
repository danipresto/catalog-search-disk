#Catalogo de HDs em powershell
$Levels = '/*'  
$alldirects = (Get-ChildItem -Directory $args[0]/$Levels -Name) 

foreach($dict in $alldirects){
    New-Item -Path $PSScriptRoot -Name "$dict" -ItemType "directory"
    $pastas = (Get-ChildItem -Directory $Path/$dict/$Levels -Name)
    foreach ($elem in $pastas){
        Write-Output $elem
        New-Item -Path $PSScriptRoot/$dict -Name "$elem" -ItemType "directory"
        Get-ChildItem -Directory $Path/$dict/$elem/$Levels -Recurse | % { $_.FullName } | Out-File $PSScriptRoot/$dict/$elem/"$elem".csv
    }
}
