#Catalogo de HDs em powershell
$Levels = '/*'  
$alldirects = (Get-ChildItem $args[0]-Name) 

foreach($dict in $alldirects){
    New-Item $PSScriptRoot -Name "$dict" -ItemType "directory"
	$nwpath = $args[0] + "/" + "$dict"
    $pastas = (Get-ChildItem $nwpath -Name)
    foreach ($elem in $pastas){
        $nnfile = $nwpath + "/" + $elem
        New-Item -Path $PSScriptRoot/$dict -Name "$elem" -ItemType "directory"
        Get-ChildItem $nnfile -Recurse | % { $_.FullName } | Out-File $PSScriptRoot/$dict/$elem/"$elem".csv
    }
}
