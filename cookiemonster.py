#!/usr/bin/env python3
import requests
import webbrowser
import os

# Define the target site
targetsite = "http://www.whatarecookies.com/cookietest.asp"

# Make the initial request to capture cookies
response = requests.get(targetsite)
cookies = response.cookies

def bringforthcookiemonster():
    # Fun ASCII art of the Cookie Monster
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
    ''')

# Display the Cookie Monster
bringforthcookiemonster()

# Show captured cookies
print(f"Target site is {targetsite}")
print(f"Cookies from the site: {cookies}")

# Send the cookie back to the site
response_with_cookie = requests.get(targetsite, cookies=cookies)

# Save the response to an HTML file
html_content = response_with_cookie.text
file_name = "response.html"
with open(file_name, "w") as file:
    file.write(html_content)

# Open the saved HTML file with Firefox (or your default browser if Firefox is not available)
try:
    # Attempt to open with Firefox specifically
    firefox_path = "/usr/bin/firefox" # Path to Firefox, adjust if necessary
    webbrowser.get(firefox_path).open(file_name)
except:
    # Fallback to the default browser if Firefox can't be opened
    webbrowser.open('file://' + os.path.realpath(file_name))

