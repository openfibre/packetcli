#!/usr/bin/env python3
from scapy.all import *
import random


def resolve_domain(domain):
    """Resolve domain to IP using DNS"""
    dns_pkt = IP(dst="8.8.8.8")/UDP(sport=RandShort(), dport=53)/DNS(rd=1, qd=DNSQR(qname=domain))
    dns_resp = sr1(dns_pkt, timeout=2)
    if dns_resp and dns_resp.haslayer(DNS) and dns_resp[DNS].ancount > 0:
        return dns_resp[DNS].an[0].rdata
    return None


def test_icmp(count=1):
    conf.verb = 0

    print("Testing ICMP reachability...")
    print("-" * 40)

    # Mix of direct IPs and popular domains
    all_targets = [
        "1.1.1.1", "8.8.8.8", "1.0.0.1",
        "google.com", "cloudflare.com", "example.com",
        "github.com", "amazon.com", "microsoft.com",
        "facebook.com", "apple.com", "netflix.com"
    ]
    if count < len(all_targets):
        icmp_targets = random.sample(all_targets, count)
    else:
        icmp_targets = all_targets

    icmp_ok = False

    for target in icmp_targets:
        # Check if target is a domain (contains letters)
        if any(c.isalpha() for c in target):
            ip = resolve_domain(target)
            if ip:
                print(f"  {target} [{ip}]", end=" ")
                pkt = IP(dst=ip)/ICMP()
                if sr1(pkt, timeout=2):
                    icmp_ok = True
                    print("OK")
                else:
                    print("Timeout")
            else:
                print(f"  {target} [Failed to resolve]")
        else:
            print(f"  {target}", end=" ")
            pkt = IP(dst=target)/ICMP()
            if sr1(pkt, timeout=2):
                icmp_ok = True
                print("OK")
            else:
                print("Timeout")

    print("-" * 40)
    return icmp_ok
