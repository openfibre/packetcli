#!/usr/bin/env python3
from scapy.all import *
from src.icmp import test_icmp
from src.dns import test_dns
from src.tcp import test_tcp


def test_all():
    print("Testing network connectivity...")
    print("=" * 40)

    icmp_ok = test_icmp()
    print()
    dns_ok = test_dns()
    print()
    tcp_ok = test_tcp()

    print("\n" + "=" * 40)
    print("\nResults:")
    print(f"  ICMP: {'OK' if icmp_ok else 'FAIL'}")
    print(f"  DNS : {'OK' if dns_ok else 'FAIL'}")
    print(f"  TCP : {'OK' if tcp_ok else 'FAIL'}")

    if icmp_ok and dns_ok and tcp_ok:
        print("\nInternet status: WORKING")
    else:
        print("\nInternet status: DEGRADED or NOT WORKING")
