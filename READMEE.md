# CodeAlpha Task 1: Basic Network Sniffer

## Project Overview
This project implements a basic network sniffer using Python and Scapy. It captures network packets and displays source IP addresses, destination IP addresses, protocols, packet sizes, and a small hexadecimal preview of available payload data.

## Tools Used
- Python 3.13.5
- Scapy
- Npcap
- Windows 11

## Features
- Captures a limited number of network packets
- Identifies IPv4 and IPv6 addresses
- Identifies TCP, UDP, and ICMP protocols
- Displays packet size
- Displays a short hexadecimal payload preview when available

## How to Run
1. Install Python and Npcap.
2. Install Scapy using `python -m pip install scapy`.
3. Open PowerShell as Administrator.
4. Navigate to the project folder.
5. Run `python sniffer.py`.

## Learning Outcome
I practiced basic packet capture and network traffic analysis using Python and Scapy.

## Safety
Run packet capture only on systems and networks you own or are authorized to monitor. This project does not decrypt encrypted traffic.
