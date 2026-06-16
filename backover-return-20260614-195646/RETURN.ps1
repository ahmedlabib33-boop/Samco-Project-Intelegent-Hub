$repo = 'C:\Users\pc\OneDrive\Documents\Project Intelligence Hub'
$backup = 'C:\Users\pc\OneDrive\Documents\Project Intelligence Hub\backover-return-20260614-195646'
Copy-Item -LiteralPath (Join-Path $backup 'dashboard.py') -Destination (Join-Path $repo 'dashboard.py') -Force
Copy-Item -LiteralPath (Join-Path $backup 'evaluate_delay_tia.py') -Destination (Join-Path $repo 'scripts\evaluate_delay_tia.py') -Force
Copy-Item -LiteralPath (Join-Path $backup 'steel_delay_tia.py') -Destination (Join-Path $repo 'src\construction_system\steel_delay_tia.py') -Force
Remove-Item -LiteralPath (Join-Path $repo 'steel_delay_tia_templates') -Recurse -Force
Copy-Item -LiteralPath (Join-Path $backup 'steel_delay_tia_templates') -Destination (Join-Path $repo 'steel_delay_tia_templates') -Recurse -Force
Write-Output 'Returned Project Intelligence Hub Delay TIA files to backover-return-20260614-195646.'
