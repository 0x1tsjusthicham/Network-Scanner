# Network Scanner
import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="network_ip", help="To enter device IP or range IP")
    options, arguments = parser.parse_args()

    return options


def scan(network_ip):
    arp_request = scapy.ARP(pdst=network_ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_brodcast_request = arp_broadcast/arp_request


    #print(arp_request.summary())
    #scapy.ls(arp_request)

    answered = scapy.srp(arp_brodcast_request, timeout=1, verbose=False)[0]

    for ans in answered:
        print(ans[1].psrc + " " + ans[1].hwsrc)


options = get_arguments()
scan(options.network_ip)