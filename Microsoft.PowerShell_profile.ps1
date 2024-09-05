function run {
    param([string]$file)

    $extension = [System.IO.Path]::GetExtension($file)

    switch ($extension) {
        ".py" { python $file; break }
        ".js" { node $file; break }
        ".ts" { bun run $file; break }
        default { Write-Host "Unsupported file type. Only .py and .js files are supported." }
    }
}


function download {
     python "C:\Scripts\download.py" 
}