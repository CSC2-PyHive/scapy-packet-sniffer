from scapy.all import sniff

# Callback function to process each packet
def packet_callback(packet):
    print(packet.summary())  # Print a summary of each captured packet

# Start sniffing packets on all interfaces
sniff(prn=packet_callback, count=10)  # Capture 10 packets; remove count to capture indefinitely
