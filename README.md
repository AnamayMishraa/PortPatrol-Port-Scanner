# PortPatrol:Port Scanner

#### Note: This tool is intended for educational purposes only. Please ensure you have permission before scanning any network or device.
A simple Python-based port scanner that allows users to scan specific ports on a given host or automatically scan common ports if none are specified.

## Features

- Scan specific ports provided by the user.
- Automatically scan a list of common ports if none are specified.
- Provides feedback on whether ports are open or closed.
- Includes error handling and resource management.

## Prerequisites

- Python 3.x

## Installation
- ### CLI Version
1. Clone the repository:
    ```sh
    git clone https://github.com/AnamayMishraa/port-scanner
    ```
2. Navigate to the project directory:
    ```sh
    cd port-scanner
    ```
- ### EXE Version
  - Extract the file `portscanner.rar` using winrar.
  - Navigate to `dist` folder.
  - Run `main.exe` file...

## Usage

1. Run the port scanner:
    ```sh
    python port_scanner.py
    ```
2. Enter the IP address you want to scan.
3. Enter the port numbers you want to scan, separated by commas (e.g., `80, 443, 8080`). If you press Enter without specifying any ports, the scanner will automatically scan common ports.

## Example

```sh
Enter the IP to perform scan: 192.168.1.1
Enter the port numbers (comma-separated) or press Enter to scan common ports: 80, 443, 22
Scanning host 192.168.1.1 on ports: [80, 443, 22]
Port 80 is open
Port 443 is open
Port 22 is closed
```
## Common Ports Scanned by Default
If no ports are specified, the following common ports will be scanned:

- 21 (FTP)
- 22 (SSH)
- 23 (Telnet)
- 25 (SMTP)
- 53 (DNS)
- 80 (HTTP)
- 110 (POP3)
- 139 (NetBIOS)
- 143 (IMAP)
- 443 (HTTPS)
- 445 (Microsoft-DS)
- 993 (IMAPS)
- 995 (POP3S)
- 3306 (MySQL)
- 3389 (RDP)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
