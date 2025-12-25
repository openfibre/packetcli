#!/usr/bin/env python3
from scapy.all import *


def test_dns():
    conf.verb = 0

    print("Testing DNS resolution...")
    print("-" * 40)

    dns_targets = ["example.com", "google.com", "cloudflare.com"]
    dns_ok = False

    for domain in dns_targets:
        dns_pkt = (
            IP(dst="8.8.8.8") /
            UDP(sport=RandShort(), dport=53) /
            DNS(rd=1, qd=DNSQR(qname=domain))
        )
        dns_resp = sr1(dns_pkt, timeout=2)
        if dns_resp and dns_resp.haslayer(DNS) and dns_resp[DNS].ancount > 0:
            dns_ok = True
            print(f"  [{domain}] OK")
            break
        else:
            print(f"  [{domain}] Timeout")

    print("-" * 40)
    print(f"\nDNS: {'OK' if dns_ok else 'FAIL'}")

    return dns_ok
