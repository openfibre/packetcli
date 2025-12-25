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


def test_tcp(count=1):
    conf.verb = 0

    print("Testing TCP connectivity...")
    print("-" * 40)

    all_targets = [
        ("1.1.1.1", 443), ("8.8.8.8", 443), ("1.0.0.1", 443),
        ("google.com", 443), ("cloudflare.com", 443),
        ("github.com", 443), ("amazon.com", 443),
        ("microsoft.com", 443), ("apple.com", 443),
        ("facebook.com", 443), ("twitter.com", 443),
        ("linkedin.com", 443), ("netflix.com", 443)
    ]

    if count < len(all_targets):
        tcp_targets = random.sample(all_targets, count)
    else:
        tcp_targets = all_targets

    tcp_ok = False

    for target, port in tcp_targets:
        # Check if target is a domain (contains letters)
        if any(c.isalpha() for c in target):
            ip = resolve_domain(target)
            if ip:
                print(f"  {target}:{port} [{ip}]", end=" ")
                tcp_pkt = IP(dst=ip)/TCP(
                    sport=RandShort(),
                    dport=port,
                    flags="S",
                    seq=1000
                )

                tcp_resp = sr1(tcp_pkt, timeout=2)
                if tcp_resp and tcp_resp.haslayer(TCP):
                    if tcp_resp[TCP].flags & 0x12:  # SYN-ACK
                        tcp_ok = True
                        print("OK")
                    else:
                        print("No SYN-ACK")
                else:
                    print("Timeout")
            else:
                print(f"  {target}:{port} [Failed to resolve]")
        else:
            print(f"  {target}:{port}", end=" ")
            tcp_pkt = IP(dst=target)/TCP(
                sport=RandShort(),
                dport=port,
                flags="S",
                seq=1000
            )

            tcp_resp = sr1(tcp_pkt, timeout=2)
            if tcp_resp and tcp_resp.haslayer(TCP):
                if tcp_resp[TCP].flags & 0x12:  # SYN-ACK
                    tcp_ok = True
                    print("OK")
                else:
                    print("No SYN-ACK")
            else:
                print("Timeout")

    print("-" * 40)
    return tcp_ok
