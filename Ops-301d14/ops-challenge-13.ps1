# This is a PowerShell script for creating multiple users in Active Directory (AD).

# First, we define a function to create new users. This helps avoid repetitive code since the process for creating each user is similar.
function Create-NewUser {
    param (
        # These are the parameters our function will accept, representing the new user's details.
        [Parameter(Mandatory=$true)][string]$samAccountName,
        [Parameter(Mandatory=$true)][string]$name,
        [Parameter(Mandatory=$true)][string]$givenName,
        [Parameter(Mandatory=$true)][string]$surname,
        [Parameter(Mandatory=$true)][string]$department,
        [Parameter(Mandatory=$true)][string]$userPrincipalName,
        [Parameter(Mandatory=$true)][string]$title
    )

    # Here we build a hash table of parameters that the New-ADUser cmdlet will use to create the user.
    $userParams = @{
        SamAccountName = $samAccountName
        Name = $name
        GivenName = $givenName
        Surname = $surname
        Department = $department
        Path = "OU=$department,DC=GlobeX,DC=local" # The OU where the user will be created.
        AccountPassword = (ConvertTo-SecureString 'Nico1234' -AsPlainText -Force) # The password for the user, converted to a secure string.
        UserPrincipalName = $userPrincipalName
        Enabled = $true # This enables the account immediately upon creation.
        ChangePasswordAtLogon = $false # The user will not be required to change their password at first login.
        Title = $title
    }

    # Create the user with the parameters we've defined.
    New-ADUser @userParams
    # Add the user to a group within their department.
    Add-ADGroupMember -Identity "${department} Group" -Members $samAccountName
}

# Before we can create users, we need to ensure that the OUs and groups they will belong to exist.
# The following commands attempt to create these OUs and groups, ignoring errors if they already exist.
# The 'ErrorAction SilentlyContinue' parameter tells PowerShell to proceed without showing errors if the OU or group already exists.
New-ADOrganizationalUnit -Name 'Sales Department' -Path 'DC=GlobeX,DC=local' -ErrorAction SilentlyContinue
New-ADOrganizationalUnit -Name 'HR' -Path 'DC=GlobeX,DC=local' -ErrorAction SilentlyContinue
New-ADOrganizationalUnit -Name 'Finance' -Path 'DC=GlobeX,DC=local' -ErrorAction SilentlyContinue
New-ADOrganizationalUnit -Name 'IT' -Path 'DC=GlobeX,DC=local' -ErrorAction SilentlyContinue

# Similarly, we create the groups corresponding to each department.
New-ADGroup -Name 'Sales Department Group' -SamAccountName 'SalesDeptGroup' -GroupScope Global -Path 'OU=Sales Department,DC=GlobeX,DC=local' -ErrorAction SilentlyContinue
New-ADGroup -Name 'HR Group' -SamAccountName 'HRDeptGroup' -GroupScope Global -Path 'OU=HR,DC=GlobeX,DC=local' -ErrorAction SilentlyContinue
New-ADGroup -Name 'Finance Group' -SamAccountName 'FinanceDeptGroup' -GroupScope Global -Path 'OU=Finance,DC=GlobeX,DC=local' -ErrorAction SilentlyContinue
New-ADGroup -Name 'IT Group' -SamAccountName 'ITDeptGroup' -GroupScope Global -Path 'OU=IT,DC=GlobeX,DC=local' -ErrorAction SilentlyContinue

# Now, we use the function we defined above to create each user. We simply pass the user's details as arguments to the function.
Create-NewUser -samAccountName 'HopkinsF' -name 'Francis Hopkins' -givenName 'Francis' -surname 'Hopkins' -department 'Sales Department' -userPrincipalName 'HopkinsF@GlobeXUSA.com' -title 'Sr. Account Executive'
Create-NewUser -samAccountName 'WilliamsA' -name 'Amanda Williams' -givenName 'Amanda' -surname 'Williams' -department 'HR' -userPrincipalName 'WilliamsA@GlobeXUSA.com' -title 'HR Specialist'
Create-NewUser -samAccountName 'SandersJ' -name 'Jim Sanders' -givenName 'Jim' -surname 'Sanders' -department 'HR' -userPrincipalName 'SandersJ@GlobeXUSA.com' -title 'HR Manager'
Create-NewUser -samAccountName 'MorganR' -name 'Rita Morgan' -givenName 'Rita' -surname 'Morgan' -department 'Finance' -userPrincipalName 'MorganR@GlobeXUSA.com' -title 'CFO'
# For your account, 'Nick', we replace 'Your Name' with 'Nick' and use your chosen password.
Create-NewUser -samAccountName 'Nick' -name 'Nick' -givenName 'Nick' -surname 'Watson' -department 'IT' -userPrincipalName 'Nick@GlobeXUSA.com' -title 'Systems Administrator'

# The last part of the script checks to see if the users were created successfully.
$users = @('HopkinsF', 'WilliamsA', 'SandersJ', 'MorganR', 'Nick')
foreach ($user in $users) {
    $verifyUser = Get-ADUser -Identity $user -Properties * | Format-List Name,Department,Title,UserPrincipalName
    if ($verifyUser) {
        Write-Output "User $user was created successfully."
        # Output the details of the created user.
        Write-Output $verifyUser
    } else {
        Write-Output "User creation for $user failed. Please check the details and try again."
    }
}


# Resources CHATGPT, LAB 13, OPS CHALLENGE 13, GITHUB