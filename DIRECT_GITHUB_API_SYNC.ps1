$Project = "C:\Users\pc\OneDrive\Documents\Project Intelligence Hub"

# =========================
# GitHub Repo Configuration
# =========================
$Owner  = "ahmedlabib33-boop"
$Repo   = "Project-Intelligence-Hub"
$Branch = "main"

# =========================
# Secure Token Input
# =========================
$TokenSecure = Read-Host "Paste GitHub token here" -AsSecureString
$BSTR = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($TokenSecure)
$TokenPlain = [Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

$Headers = @{
    Authorization = "Bearer $TokenPlain"
    Accept = "application/vnd.github+json"
    "X-GitHub-Api-Version" = "2022-11-28"
    "User-Agent" = "Project-Intelligence-Hub-Direct-API-Sync"
}

# =========================
# Local State File
# =========================
$StatePath = Join-Path $Project ".github_api_sync_state.json"

# =========================
# Exclusions - Very Important
# =========================
$ExcludeDirs = @(
    ".git",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".vscode",
    ".idea",
    "generated_outputs",
    "tmp_letters_ocr",
    "backover-return-20260614-195646"
)

$ExcludeExtensions = @(
    ".db",
    ".sqlite",
    ".sqlite3",
    ".pyc",
    ".pyo",
    ".pyd",
    ".log",
    ".err",
    ".out",
    ".vsix",
    ".bak"
)

$ExcludeFiles = @(
    ".env",
    ".env.local",
    ".github_api_sync_state.json",
    "PROJECT_DIAGNOSTIC_OUTPUT.txt",
    "NO_GIT_PROJECT_DIAGNOSTIC.txt"
)

$ExcludeRelativePaths = @(
    ".streamlit/secrets.toml"
)

$MaxFileSizeMB = 90

function ConvertTo-GitHubPathUri($RelativePath) {
    return (($RelativePath -split "/") | ForEach-Object {
        [System.Uri]::EscapeDataString($_)
    }) -join "/"
}

function Should-Exclude($File, $RelativePath) {
    $parts = $RelativePath -split "/"

    foreach ($dir in $ExcludeDirs) {
        if ($parts -contains $dir) {
            return $true
        }
    }

    if ($RelativePath -like "backover-return-*/*") {
        return $true
    }

    if ($ExcludeExtensions -contains $File.Extension.ToLower()) {
        return $true
    }

    if ($ExcludeFiles -contains $File.Name) {
        return $true
    }

    if ($ExcludeRelativePaths -contains $RelativePath) {
        return $true
    }

    if ($File.Length -gt ($MaxFileSizeMB * 1024 * 1024)) {
        return $true
    }

    return $false
}

function Get-State {
    if (!(Test-Path $StatePath)) {
        return @{}
    }

    $raw = Get-Content $StatePath -Raw

    if ([string]::IsNullOrWhiteSpace($raw)) {
        return @{}
    }

    $obj = $raw | ConvertFrom-Json
    $hash = @{}

    foreach ($p in $obj.PSObject.Properties) {
        $hash[$p.Name] = $p.Value
    }

    return $hash
}

function Save-State($State) {
    $State | ConvertTo-Json -Depth 20 | Set-Content $StatePath -Encoding UTF8
}

function Test-GitHubRepoAccess {
    $repoUrl = "https://api.github.com/repos/$Owner/$Repo"

    try {
        $repoInfo = Invoke-RestMethod -Method Get -Uri $repoUrl -Headers $Headers
        Write-Host "Repo access OK: $($repoInfo.full_name)" -ForegroundColor Green
    }
    catch {
        Write-Host "Repo access failed." -ForegroundColor Red
        Write-Host "Check Owner, Repo name, token permission, and branch." -ForegroundColor Yellow
        throw
    }
}

function Upload-Or-Update-File($File, $RelativePath) {
    $apiPath = ConvertTo-GitHubPathUri $RelativePath
    $url = "https://api.github.com/repos/$Owner/$Repo/contents/$apiPath"

    $existingSha = $null

    try {
        $existing = Invoke-RestMethod -Method Get -Uri "$url`?ref=$Branch" -Headers $Headers
        $existingSha = $existing.sha
    }
    catch {
        $existingSha = $null
    }

    $bytes = [System.IO.File]::ReadAllBytes($File.FullName)
    $base64 = [Convert]::ToBase64String($bytes)

    $body = @{
        message = "API sync: $RelativePath"
        content = $base64
        branch  = $Branch
    }

    if ($existingSha) {
        $body.sha = $existingSha
    }

    $json = $body | ConvertTo-Json -Depth 10

    Invoke-RestMethod -Method Put -Uri $url -Headers $Headers -Body $json -ContentType "application/json" | Out-Null
}

# =========================
# Start Sync
# =========================
try {
    Set-Location $Project

    Write-Host ""
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host "Project Intelligence Hub - GitHub API Sync" -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host "Project: $Project"
    Write-Host "Repo:    $Owner/$Repo"
    Write-Host "Branch:  $Branch"
    Write-Host ""

    Test-GitHubRepoAccess

    $OldState = Get-State
    $NewState = @{}

    $Files = Get-ChildItem $Project -Recurse -File | ForEach-Object {
        $rel = [System.IO.Path]::GetRelativePath($Project, $_.FullName).Replace("\", "/")

        if (!(Should-Exclude $_ $rel)) {
            [PSCustomObject]@{
                File = $_
                RelativePath = $rel
            }
        }
    }

    Write-Host ""
    Write-Host "Files selected for sync: $($Files.Count)" -ForegroundColor Cyan
    Write-Host ""

    $Uploaded = 0
    $Skipped = 0
    $Failed = 0

    foreach ($item in $Files) {
        $file = $item.File
        $relative = $item.RelativePath

        $localHash = (Get-FileHash $file.FullName -Algorithm SHA256).Hash
        $NewState[$relative] = $localHash

        if ($OldState.ContainsKey($relative) -and $OldState[$relative] -eq $localHash) {
            Write-Host "Skipped unchanged: $relative" -ForegroundColor DarkGray
            $Skipped++
            continue
        }

        try {
            Upload-Or-Update-File $file $relative
            Write-Host "Uploaded/Updated: $relative" -ForegroundColor Green
            $Uploaded++
        }
        catch {
            Write-Host "FAILED: $relative" -ForegroundColor Red
            Write-Host $_.Exception.Message -ForegroundColor Red
            $Failed++
        }
    }

    Save-State $NewState

    Write-Host ""
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host "Direct GitHub API Sync Completed" -ForegroundColor Cyan
    Write-Host "==========================================" -ForegroundColor Cyan
    Write-Host "Uploaded/Updated: $Uploaded"
    Write-Host "Skipped unchanged: $Skipped"
    Write-Host "Failed: $Failed"

    if ($Failed -eq 0) {
        Write-Host ""
        Write-Host "SUCCESS: Project folder synced to GitHub without Git." -ForegroundColor Green
    } else {
        Write-Host ""
        Write-Host "WARNING: Some files failed. Review failed list above." -ForegroundColor Yellow
    }
}
finally {
    if ($BSTR -ne [IntPtr]::Zero) {
        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)
    }

    $TokenPlain = $null
}
