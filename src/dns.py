#!/usr/bin/env python3
from scapy.all import *
import random


def test_dns(count=1):
    conf.verb = 0

    print("Testing DNS resolution...")
    print("-" * 40)

    all_targets = [
        "example.com", "google.com", "cloudflare.com",
        "github.com", "amazon.com", "microsoft.com",
        "facebook.com", "apple.com", "netflix.com",
        "twitter.com", "linkedin.com", "yahoo.com",
        "wikipedia.org", "reddit.com", "stackoverflow.com"
    ]
    if count < len(all_targets):
        dns_targets = random.sample(all_targets, count)
    else:
        dns_targets = all_targets

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
            print(f"  {domain} OK")
        else:
            print(f"  {domain} Timeout")

    print("-" * 40)
    return dns_ok
