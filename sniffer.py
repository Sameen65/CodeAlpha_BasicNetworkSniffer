
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw

def analyze_packet(packet):
    source = "Unknown"
    destination = "Unknown"
    protocol = "Other"

    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst
    elif IPv6 in packet:
        source = packet[IPv6].src
        destination = packet[IPv6].dst

    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"

    print("-" * 50)
    print("Source IP:", source)
    print("Destination IP:", destination)
    print("Protocol:", protocol)
    print("Packet size:", len(packet), "bytes")

    if Raw in packet:
        payload = bytes(packet[Raw].load)
        print("Payload (first 16 bytes, hex):", payload[:16].hex())

print("CodeAlpha Network Sniffer")
print("Capturing 10 packets...")
sniff(count=10, prn=analyze_packet, store=False)
