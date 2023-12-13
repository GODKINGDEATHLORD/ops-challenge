#!/usr/bin/env python3
import requests

# Function to translate status codes to human-readable messages
def translate_status_code(code):
    status_codes = {
        200: "OK - The request was successful.",
        201: "Created - The request was successful and a resource was created.",
        400: "Bad Request - The request could not be understood by the server due to malformed syntax.",
        401: "Unauthorized - The request requires user authentication.",
        403: "Forbidden - The server understood the request, but is refusing to fulfill it.",
        404: "Not Found - The server has not found anything matching the Request-URI.",
        500: "Internal Server Error - The server encountered an unexpected condition which prevented it from fulfilling the request."
        # Add other status codes as needed
    }
    return status_codes.get(code, "Status code not recognized")

# User input for URL and HTTP method
url = input("Please enter the URL you wish to make a request to: ")
method = input("Please enter the HTTP method you wish to use (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Print the request details
print(f"You have chosen to make a {method} request to {url}.")
confirm = input("Are you sure you want to proceed? (yes/no): ")

# Execute the request if confirmed
if confirm.lower() == 'yes':
    try:
        response = requests.request(method, url)
        print(f"Response Status Code: {response.status_code} - {translate_status_code(response.status_code)}")
        print("Response Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
        print("\nResponse Body:")
        print(response.text)  # Note that for large bodies, you might want to print only a portion of it
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
else:
    print("Request cancelled.")

# Note: For POST, PUT, PATCH, you might need to send data which is not covered here.
# You'll need to modify the code to handle data input for those types of requests.
# must run this in terminal prior to  runnning : pip install requests
# sstill working on this 
