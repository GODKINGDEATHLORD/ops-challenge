import os

# Requirement: At least three variables must be declared
command1 = "whoami"
command2 = "ip a"
command3 = "lshw -short"

# Using the os module to execute Bash commands
def execute_command(command):
    print(f"Executing command: {command}")
    os.system(command)
    print("Execution complete.\n")

# Requirement: The Python function print() must be used at least three times
# Executing the commands
print("Starting the Bash commands execution...\n")
execute_command(command1)
execute_command(command2)
execute_command(command3)
print("All commands executed successfully.")

# Resources: ChatGpt , https://docs.python.org/3/library/os.html    https://www.python.org/dev/peps/pep-0008/