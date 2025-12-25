#!/usr/bin/env python3
import sys
from src.core import test_connectivity
from src.icmp import test_icmp
from src.dns import test_dns
from src.tcp import test_tcp


def main():
    if len(sys.argv) < 2:
        test_connectivity()
        return

    tool = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    if tool == "all":
        test_connectivity(count)
    elif tool == "icmp":
        result = test_icmp(count)
        print("ICMP:", "OK" if result else "FAIL")
    elif tool == "dns":
        result = test_dns(count)
        print("DNS :", "OK" if result else "FAIL")
    elif tool == "tcp":
        result = test_tcp(count)
        print("TCP :", "OK" if result else "FAIL")
    else:
        print(f"Error: Unknown tool '{tool}'")
        print("Available: all, icmp, dns, tcp")
        sys.exit(1)


if __name__ == "__main__":
    main()
