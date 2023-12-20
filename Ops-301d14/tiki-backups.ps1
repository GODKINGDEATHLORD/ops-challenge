# Source directories to back up
$sourceDirs = @(
    "C:\Users\Administrator\FINANCE",
    "C:\Users\Administrator\HR",
    "C:\Users\Administrator\IT",
    "C:\Users\Administrator\Research"
)

# Define the root backup directory on the local disk
$backupRootDir = "C:\Backups"

# Create a timestamped directory for this backup
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupDir = Join-Path $backupRootDir ("Backup_" + $timestamp)
New-Item -Path $backupDir -ItemType Directory

# Copy each source directory to the timestamped backup directory
foreach ($dir in $sourceDirs) {
    if (Test-Path $dir) {
        $folderName = Split-Path $dir -Leaf
        $destPath = Join-Path $backupDir $folderName
        Copy-Item -Path $dir -Destination $destPath -Recurse
        Write-Output "Backed up $folderName to $destPath"
    } else {
        Write-Output "Source directory $dir does not exist."
    }
}

Write-Output "Backup completed to $backupDir"
