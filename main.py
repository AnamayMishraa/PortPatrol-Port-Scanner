import socket

# Common ports to scan if the user does not provide any
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 993, 995, 3306, 3389]

def portScanner(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(7)  
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except socket.error as err:
        print(f"Socket error: {err}")
    finally:
        s.close()

def main():
    host = input("Enter the IP to perform scan: ")
    ports_input = input("Enter the port numbers (comma-separated) or press Enter to scan common ports: ")
    
    if ports_input:
        ports = [int(port.strip()) for port in ports_input.split(',')]
    else:
        ports = COMMON_PORTS

    print(f"Scanning host {host} on ports: {ports}")
    for port in ports:
        portScanner(host, port)

if __name__ == "__main__":
    main()