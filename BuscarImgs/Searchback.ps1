$contrato=$args[0]
$stringb=$args[1]

Get-ChildItem -Path .\*\$contrato\ -Recurse | Select-String $stringb