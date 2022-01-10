$contrato=$args[0]
$stringb=$args[1]
$saida=$args[2]
Get-ChildItem -Path .\*\$contrato\ -Recurse | Select-String $stringb >> $saida
