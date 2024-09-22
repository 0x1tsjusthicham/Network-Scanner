# Network Scanner
import scapy.all as scapy
# Creating a Packet

arp_request = scapy.ARP(pdst="192.168.1.1/24")
arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
arp_brodcast_request = arp_broadcast/arp_request


# Sending and receiving a packet
#print(arp_request.summary())
#scapy.ls(arp_request)

answered = scapy.srp(arp_brodcast_request, timeout=1, verbose=False)[0]

for ans in answered:
    print(ans[1].psrc + " " + ans[1].hwsrc)
# Parsing answers
# Displaying packets