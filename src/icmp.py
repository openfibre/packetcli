#!/usr/bin/env python3
from scapy.all import *


def test_icmp():
    conf.verb = 0

    icmp_targets = ["1.1.1.1", "8.8.8.8"]
    icmp_ok = False

    for target in icmp_targets:
        pkt = IP(dst=target)/ICMP()
        if sr1(pkt, timeout=2):
            icmp_ok = True
            break

    return icmp_ok
