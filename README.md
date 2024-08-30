# Scapy Packet Sniffer

This project demonstrates a simple packet sniffer built using Scapy in Python.

## Description

This script captures network traffic and displays a summary of each captured packet. It allows you to gain basic insights into the communication flowing through your network interface.

## Installation

1. **Install Python 3**: Download and install Python 3 from the official website ([https://www.python.org/downloads/](https://www.python.org/downloads/)) if you haven't already.

2. **Install Scapy**: Open a terminal and run the following command to install Scapy:

```bash
pip3 install scapy
```

3. Usage
- **Run the Sniffer**: Navigate to your project directory in the terminal and run the script with elevated privileges:

```bash
sudo python3 scapy_sniffer.py
```

**Note**: Running with `sudo` is necessary to grant the script permission to capture network traffic.

- **Observe Packet Summaries**: The script will begin capturing packets and display a summary of each capture packet on the terminal. By default, it captures 10 packets. You can remove the `count=10` argument in the script to capture packets indefinitely.
- _Remind to interrupt the running command. Press `Ctrl` and `C` simultaneously._

## Explanation of the Code

The script utilizes the `sniff` function from Scapy to capture packets and a callback function (`packet_callback`) to process each captured packet. The callback function simply prints a summary of the packet using the `packet.summary()` method.

### Here's a breakdown of the code:

`from scapy.all import sniff`: Imports the `sniff` function for packet capturing.
`packet_callback(packet)`: This function is called for each captured packet. It prints a summary of the packet using `packet.summary()`.
`sniff(prn=packet_callback, count=10)`: Starts capturing packets on all interfaces. The captured packets are passed to the `packet_callback` function. The `count` argument limits the number of captured packets to 10 (remove it for continuous capture).

### Contributing
Feel free to contribute to this project by:

- Reporting any bugs or issues you encounter.
- Suggesting improvements or additional features.
- Forking the repository and creating pull requests with your modifications.
