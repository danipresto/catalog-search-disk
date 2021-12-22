$Depth = 1
$Path = '.'

$Levels = '/*' * $Depth
$alldirects = (Get-ChildItem -Directory $Path/$Levels) #listar todos os diretórios 


$resultsB = @() #Tamanho da pasta
$resultsF = @() #Nº de Arquivos
$resultsD = @() #Nº de Diretórios

foreach($dict in $alldirects) {     #Para Cada Diretório 
    robocopy $dict \\localhost\C$\nul /l /LOG:sizes.txt /xj /e /njh /ndl /nc /ns /bytes /mt:64 | Out-Null 

    #Filtrando o log da saída do robocopy
    $directs = (Get-Content -Path .\sizes.txt)[-5].split(" ") 
    $files = (Get-Content -Path .\sizes.txt)[-6].split(" ")  
    $bytes = (Get-Content -Path .\sizes.txt)[-4].split(" ")  


    #Eliminar os espaços vazios 
    #Repete três vezes, para tamanho, arquivos e diretórios
    #Pode ser implementado uma função para evitar a repetição

    $directsN = @()
    foreach ($letter in $directs)
    {
        if ($letter -ne "") #Se não for uma string nula adicione ao vetor
        {
            $directsN = $directsN += $letter
        }
    }

    $filesN = @()
    foreach ($letter in $files)
    {
        if ($letter -ne "")
        {
            
            $filesN = $filesN += $letter
        }
    }


    $bytesN = @()
    foreach ($letter in $bytes)
    {
        if ($letter -ne "")
        {
           
            $bytesN = $bytesN += $letter
        }
    }

    $dictvalue = $dict | Select-Object -expand Name #Pega só o último nome do caminho que é o nome da pasta 
    $bvalue = $bytesN[1]
    $bvalue = $bvalue/(1000*1000*1000) #Transforma bytes para GB
    $fvalue = $filesN[1]
    $dvalue = $directsN[1]

    #Adicionando resultados ao vetor
    #Formato de saída. Ex: NomedaPasta TamanhodaPasta GBs 
    #Caso queira formatar a saída deve alterar as próximas linhas, por exemplo apagar dictvalue resulta em novo formato:
    #TamanhodaPasta GBs 

    $resultsB = $resultsB  + "$($dictvalue) $($bvalue) GBs" 
    $resultsF = $resultsF  + "$($dictvalue) $($fvalue) Arquivos"
    $resultsD = $resultsD  + "$($dictvalue) $($dvalue) Diretorios"
   

}

#Escreve resultados em um Arquivo .txt
$resultsB | Out-File -Append LOGsize.txt
$resultsF | Out-File -Append LOGsize.txt
$resultsD | Out-File -Append LOGsize.txt

#Saída do programa
#Caso queira alterar as informações da saída pode alterar 
#Por exemplo apagar resultsF e resultsD vai retornar apenas o tamanho das pastas.

return $resultsB, $resultsF, $resultsD
#LOG:sizes.txt é o arquivo de saída do robocopy 
#localhost define que é maquína local, pode ser usado ip remoto
