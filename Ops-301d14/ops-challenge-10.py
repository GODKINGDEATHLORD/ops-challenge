# Importing the os module to enable file deletion
import os

# Define the filename
filename = 'example.txt'

# Create a new .txt file and append three lines
with open(filename, 'w') as file:
    file.write("First line\n")
    file.write("Second line\n")
    file.write("Third line\n")

# Print to the screen the first line
with open(filename, 'r') as file:
    first_line = file.readline()
    print("The first line is:", first_line.strip())

# Delete the .txt file
os.remove(filename)

# Confirm deletion
if not os.path.exists(filename):
    print(f"The file {filename} has been deleted.")

# Resources Chat GPT, Demo , Challenge notes 
