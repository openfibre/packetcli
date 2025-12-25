#!/usr/bin/env python3
from src.icmp import test_icmp
from src.dns import test_dns
from src.tcp import test_tcp


def test_connectivity(count=1):
    icmp_ok = test_icmp(count)
    print()
    dns_ok = test_dns(count)
    print()
    tcp_ok = test_tcp(count)

    # ---------- Final verdict ----------
    print("\n" + "=" * 40)
    print("ICMP:", "OK" if icmp_ok else "FAIL")
    print("DNS :", "OK" if dns_ok else "FAIL")
    print("TCP :", "OK" if tcp_ok else "FAIL")

    if icmp_ok and dns_ok and tcp_ok:
        print("\nInternet status: WORKING")
    else:
        print("\nInternet status: DEGRADED or NOT WORKING")
