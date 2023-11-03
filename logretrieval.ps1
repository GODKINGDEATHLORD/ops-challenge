# Function to output all events from the System event log that occurred in the last 24 hours to a file named last_24.txt on the desktop.
Function Export-Last24HoursEventsToFile {
    Get-EventLog -LogName System -After (Get-Date).AddDays(-1) | Out-File "$env:USERPROFILE\Desktop\last_24.txt"
}

# Function to output all "error" type events from the System event log to a file named errors.txt on the desktop.
Function Export-ErrorEventsToFile {
    Get-EventLog -LogName System -EntryType Error | Out-File "$env:USERPROFILE\Desktop\errors.txt"
}

# Function to print to the screen all events with ID of 16 from the System event log.
Function Print-EventsWithID16 {
    Get-EventLog -LogName System -InstanceId 16
}

# Function to print to the screen the most recent 20 entries from the System event log.
Function Print-MostRecent20Entries {
    Get-EventLog -LogName System -Newest 20
}

# Function to print to the screen all sources of the 500 most recent entries in the System event log with full lines displayed.
Function Print-500MostRecentEntriesWithFullLines {
    Get-EventLog -LogName System -Newest 500 | Format-Table -Wrap -AutoSize
}

# Main function that calls the individual functions.
Function Main {
    Export-Last24HoursEventsToFile
    Export-ErrorEventsToFile
    Print-EventsWithID16
    Print-MostRecent20Entries
    Print-500MostRecentEntriesWithFullLines
}

# Call the main function to execute the tasks.
Main
