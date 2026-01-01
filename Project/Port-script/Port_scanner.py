import socket

# Common ports and their services
SERVICES = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

def scan_ports(target, ports):
    print("\n" + "=" * 45)
    print(f"  Scanning Target: {target}")
    print("=" * 45 + "\n")

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        try:
            result = s.connect_ex((target, port))
            service = SERVICES.get(port, "Unknown")

            if result == 0:
                print(f"[+] Port {port:<5} ({service}) : OPEN")
            else:
                print(f"[-] Port {port:<5} ({service}) : CLOSED")

        except socket.gaierror:
            print("[!] Error: Hostname could not be resolved.")
            break

        except socket.error:
            print("[!] Error: Could not connect to the target.")
            break

        finally:
            s.close()

    print("\nScan completed.")

def main():
    target = input("Enter target IP or hostname: ").strip()
    ports = [21, 22, 80, 443]
    scan_ports(target, ports)

if __name__ == "__main__":
    main()

