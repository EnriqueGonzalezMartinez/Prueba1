param(
    [Parameter(Mandatory)] [string] $path, [string] $file
)
if ($file -eq ''){
    if (Test-Path -Path $path){
        if ((Get-Item $path) -is [System.IO.DirectoryInfo]){
            Get-ChildItem $path | Get-FileHash | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders
        }else{
            Get-FileHash -Algorithm SHA256 -Path $path | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders
        }
    }else{
        Write-Host "El path no existe."
    }
    
}else{

    if (Test-Path -Path $path){
        if ((Get-Item $path) -is [System.IO.DirectoryInfo]){
            Get-ChildItem $path | Get-FileHash | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File $file -Encoding ascii -ErrorAction SilentlyContinue
            Write-Host "El archivo se creó correctamente."
        }else{
            Get-FileHash -Algorithm SHA256 -Path $path | Select-Object -Property Hash, Path | Format-Table -HideTableHeaders | Out-File $file -Encoding ascii
            Write-Host "El archivo se creó correctamente."
        }
    }else{
        Write-Host "El path no existe."
    }
}