
# Network Scanner

This Python script scans the devices on a network and retrieves their IP and MAC addresses. It utilizes the **Scapy** library to send ARP (Address Resolution Protocol) requests to devices on the network and collects the responses to identify active hosts.

## How It Works
The script performs the following:
- Sends ARP requests over the network to the specified IP address or range of IPs.
- Captures the responses from devices on the network.
- Extracts and displays the IP and MAC addresses of the devices.

## Prerequisites

Before running this script, ensure you have:
- **Python 3.x** installed
- **Scapy** installed

To install Scapy, you can use `pip`:
```bash
pip install scapy
```

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/0x1tsjusthicham/Network-Scanner.git
   cd Network-Scanner
   ```

2. **Run the script**:
   The script requires a network IP or a range of IPs to scan. You can provide the IP or range using the `-r` or `--range` option.

   ```bash
   sudo python3 network_scanner.py -r [network_ip]
   ```

   - Replace `[network_ip]` with the IP address or range of IP addresses you want to scan (e.g., `192.168.1.1/24` for the whole subnet).

### Example:

```bash
sudo python3 network_scanner.py -r 192.168.1.1/24
```

This will scan all devices in the `192.168.1.x` network and return their IP and MAC addresses.

### Sample Output:
```bash
IP Address           MAC Address
------------------------------------------
192.168.1.2          00:11:22:33:44:55
192.168.1.3          00:aa:bb:cc:dd:ee
```

## Options
- `-r`, `--range`: Specifies the IP address or IP range to scan.

## Code Overview

1. **`get_arguments()`**: This function parses command-line arguments to get the network IP or range provided by the user.
2. **`scan()`**: This function performs the ARP scan on the network and collects the IP and MAC addresses of the devices.
3. **`display_clients()`**: This function displays the scanned devices in a user-friendly format.

## Notes

- The script uses **ARP**, so it requires root privileges to run. Always use `sudo` when executing the script.
- The script only detects devices that respond to ARP requests, which typically includes most devices on a local network.

## License
@itsjusthicham
