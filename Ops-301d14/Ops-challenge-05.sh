#!/bin/bash

# Define log files and backup directory
LOG_FILES=("/var/log/syslog" "/var/log/wtmp")
BACKUP_DIR="/var/log/backups"

# Ensure backup directory exists
mkdir -p "$BACKUP_DIR"

# Loop through each log file
for file in "${LOG_FILES[@]}"; do
    if [ -f "$file" ]; then
        # Print file size before compression
        FILE_SIZE_BEFORE=$(stat -c%s "$file")
        echo "File size of $file before compression: $FILE_SIZE_BEFORE bytes"

        # Compress and backup the log file
        TIMESTAMP=$(date +"%Y%m%d%H%M%S")
        gzip -c "$file" > "$BACKUP_DIR/$(basename "$file")-$TIMESTAMP.gz"

        # Clear the contents of the log file
        # Truncating instead of deleting to retain file with permissions
        > "$file"

        # Print file size after compression
        COMPRESSED_FILE="$BACKUP_DIR/$(basename "$file")-$TIMESTAMP.gz"
        if [ -f "$COMPRESSED_FILE" ]; then
            FILE_SIZE_AFTER=$(stat -c%s "$COMPRESSED_FILE")
            echo "File size of $COMPRESSED_FILE: $FILE_SIZE_AFTER bytes"
        else
            echo "Compression failed for $file"
        fi
    else
        echo "File $file does not exist."
    fi

done

# Resources: Chatgpt, Github 