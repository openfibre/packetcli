#!/usr/bin/env python3
from scapy.all import *


def test_tcp():
    conf.verb = 0

    print("Testing TCP connectivity...")
    print("-" * 40)

    tcp_ok = False
    tcp_pkt = IP(dst="1.1.1.1")/TCP(
        sport=RandShort(),
        dport=443,
        flags="S",
        seq=1000
    )

    tcp_resp = sr1(tcp_pkt, timeout=2)
    if tcp_resp and tcp_resp.haslayer(TCP):
        if tcp_resp[TCP].flags & 0x12:  # SYN-ACK
            tcp_ok = True
            print(f"  [1.1.1.1:443] OK")
    else:
        print(f"  [1.1.1.1:443] Timeout")

    print("-" * 40)
    print(f"\nTCP: {'OK' if tcp_ok else 'FAIL'}")

    return tcp_ok
