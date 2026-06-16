cd "C:\Users\pc\OneDrive\Documents\Project Intelligence Hub"

git add .

$changes = git status --porcelain

if ($changes) {
    $msg = "Auto sync Project Intelligence Hub - " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    git commit -m "$msg"
    git push origin main
} else {
    Write-Host "No changes to sync."
}
