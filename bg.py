import subprocess

def grab_banner_netcat(ip, port):
    try:
        result = subprocess.check_output(['nc', '-v', '-n', '-w1', ip, str(port)], stderr=subprocess.STDOUT)
        print(f"Netcat banner grabbing result:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Netcat banner grabbing error:\n{e.output.decode()}")

def grab_banner_telnet(ip, port):
    try:
        result = subprocess.check_output(f'echo "" | telnet {ip} {port}', shell=True, stderr=subprocess.STDOUT)
        print(f"Telnet banner grabbing result:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Telnet banner grabbing error:\n{e.output.decode()}")

def grab_banner_nmap(ip):
    try:
        result = subprocess.check_output(['nmap', '-sV', ip], stderr=subprocess.STDOUT)
        print(f"Nmap banner grabbing result:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Nmap banner grabbing error:\n{e.output.decode()}")

def main():
    ip = input("Enter the target IP or URL: ")
    port = input("Enter the target port number: ")
    print("Performing banner grabbing using Netcat...")
    grab_banner_netcat(ip, port)
    print("\nPerforming banner grabbing using Telnet...")
    grab_banner_telnet(ip, port)
    print("\nPerforming banner grabbing using Nmap (this may take a while)...")
    grab_banner_nmap(ip)

if __name__ == "__main__":
    main()
