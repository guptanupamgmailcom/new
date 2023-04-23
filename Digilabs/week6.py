
import scapy

from scapy.all import *

# Perform a traceroute
traceroute_result = traceroute("www.google.com")

# Print the results
print(traceroute_result)

# Detect IP spoofing
def detect_ip_spoof(pkt):
    if IP in pkt:
        # Check if the source IP address is from a private IP range
        if pkt[IP].src.startswith("10.") or pkt[IP].src.startswith("172.16.") or pkt[IP].src.startswith("192.168."):
            print("Possible IP spoofing attempt detected from IP address: {}".format(pkt[IP].src))

# Sniff network traffic and pass it to the detect_ip_spoof function
sniff(prn=detect_ip_spoof)