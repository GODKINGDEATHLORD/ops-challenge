# Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
Get-Process | Sort-Object CPU -Descending | Format-Table -Property Name, CPU -AutoSize

# Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
Get-Process | Sort-Object Id -Descending | Format-Table -Property Name, Id -AutoSize

# Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5 | Format-Table -Property Name, WorkingSet -AutoSize

# Start a browser process (such as Google Chrome or MS Edge) and have it open https://owasp.org/www-project-top-ten/.
Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://owasp.org/www-project-top-ten/"
# Note: Update the file path to the browser executable according to your system.

# Start the process Notepad ten times using a for loop.
for ($i = 1; $i -le 10; $i++) {
    Start-Process -FilePath "notepad.exe"
}

# Close all instances of Notepad.
Get-Process | Where-Object { $_.Name -eq "notepad" } | ForEach-Object { Stop-Process -Id $_.Id }

# Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Google Chrome or MS Edge.
$processToKill = Get-Process -Name "chrome" # or "msedge"
if ($processToKill -ne $null) {
    Stop-Process -Id $processToKill.Id
}
