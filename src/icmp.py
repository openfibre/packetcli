#!/usr/bin/env python3
from scapy.all import *


def test_icmp():
    conf.verb = 0

    print("Testing ICMP reachability...")
    print("-" * 40)

    icmp_targets = ["1.1.1.1", "8.8.8.8"]
    icmp_ok = False

    for target in icmp_targets:
        pkt = IP(dst=target)/ICMP()
        if sr1(pkt, timeout=2):
            icmp_ok = True
            print(f"  [{target}] OK")
            break
        else:
            print(f"  [{target}] Timeout")

    print("-" * 40)
    print(f"\nICMP: {'OK' if icmp_ok else 'FAIL'}")

    return icmp_ok
