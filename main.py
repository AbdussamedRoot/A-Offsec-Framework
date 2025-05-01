import socket

def domain_to_ip(domain):
    """
    Resolves a domain name to its IP address.
    """
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP address of {domain}: {ip}")
    except socket.gaierror:
        print("[-] Error: Unable to resolve the domain name.")

def port_scanner(target_ip, start_port, end_port):
    """
    Scans for open ports on a target IP address.
    """
    print(f"Scanning ports {start_port} to {end_port} on {target_ip}...")
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((target_ip, port))
                print(f"[+] Port {port} is open.")
        except:
            pass
    print("Scan complete.")



def start_listener(port):
    """
    Starts a reverse shell listener on the specified port.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print(f"Listening on port {port}...")
        conn, addr = s.accept()
        print(f"[+] Connection established from {addr}")
        while True:
            command = input("Shell> ")
            if command.lower() == "exit":
                conn.send(b"exit")
                break
            conn.send(command.encode())
            response = conn.recv(4096).decode()
            print(response)

def main_menu():
    """
    Displays the main menu and returns the user's choice.
    """
    print("=" * 50)
    print("A-OffSec - Offensive Security Toolkit".center(50))
    print("=" * 50)
    print("1. Domain-to-IP Scanner")
    print("2. Port Scanner")
    print("3. Reverse Shell Listener")
    print("4. Exit")
    print("=" * 50)

    choice = input("Select an option: ").strip()
    return choice

def main():
    """
    Main function to handle user input and execute the selected tool.
    """
    while True:
        choice = main_menu()
        if choice == "1":
            domain = input("Enter the domain name: ").strip()
            domain_to_ip(domain)
        elif choice == "2":
            target_ip = input("Enter the target IP address: ").strip()
            start_port = int(input("Enter the start port: "))
            end_port = int(input("Enter the end port: "))
            port_scanner(target_ip, start_port, end_port)
        elif choice == "3":
            port = int(input("Enter the port to listen on: "))
            start_listener(port)
        elif choice == "4":
            print("Exiting A-OffSec. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()