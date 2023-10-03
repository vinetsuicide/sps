import socket
from colorama import Fore, Style
import pyfiglet
import argparse

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.2)
    result = sock.connect_ex((target, port))
    sock.close()
    return result == 0

def get_ip(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except:
        return None

def perform_scan(ip):
    open_ports = []
    ports = range(1, 1024)  # change if u want
    print(f"\nScanning {ip}...\n")

    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
            print(f"\r{Fore.GREEN}[+] Port {port} is open{Style.RESET_ALL}", end='')

    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target IP address or domain name")
    args = parser.parse_args()

    target = args.target

    ip = get_ip(target)

    if ip is None:
        print(f"Error: Could not resolve the target '{target}' to an IP address.")
        return

    ascii_title = pyfiglet.figlet_format("-SPS-")
    print(f"{Fore.RED}{ascii_title}{Style.RESET_ALL}")

    open_ports = perform_scan(ip)

    if open_ports:
        print(f"\n\n{Fore.GREEN}[+] Open Ports:{Style.RESET_ALL}")
        for port in open_ports:
            print(f"{Fore.GREEN}  - Port {port} is open{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}[-] No open ports found{Style.RESET_ALL}")

if __name__ == "__main__":
    main()

