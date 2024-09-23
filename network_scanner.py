# Network Scanner
import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="network_ip", help="To enter device IP or range IP")
    options, arguments = parser.parse_args()

    if not options.network_ip:
        parser.error("[-] PLease specify an ip address, -h for help")

    return options


def scan(network_ip):
    arp_request = scapy.ARP(pdst=network_ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_brodcast_request = arp_broadcast/arp_request


    #print(arp_request.summary())
    #scapy.ls(arp_request)

    answered = scapy.srp(arp_brodcast_request, timeout=1, verbose=False)[0]

    clients_list = []
    for ans in answered:
        client_dict = {"IP": ans[1].psrc, "MAC":ans[1].hwsrc}
        clients_list.append(client_dict)
    
    return clients_list

def display_clients(clients):
    print("IP Address\t\t MAC Address")
    print("-" * 42)
    for client in clients:
        print(client["IP"], "\t\t", client["MAC"])

options = get_arguments()
clients = scan(options.network_ip)
display_clients(clients)