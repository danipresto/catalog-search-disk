robocopy $args[0] \\localhost\C$\nul /l /LOG:sizes.txt /xj /e /np /nfl /ndl /njh /bytes /mt:64 | Select-Object -Last 4
Write-Output $args[0]

#args é o contrato, definido no arquivo python 
#LOG:sizes.txt é o arquivo de saída do programa 
#localhost define que é maquína local, pode ser usado ip remoto