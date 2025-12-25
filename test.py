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

    if tool == "icmp":
        result = test_icmp()
        print("ICMP:", "OK" if result else "FAIL")
    elif tool == "dns":
        result = test_dns()
        print("DNS :", "OK" if result else "FAIL")
    elif tool == "tcp":
        result = test_tcp()
        print("TCP :", "OK" if result else "FAIL")
    else:
        print(f"Error: Unknown tool '{tool}'")
        print("Available: icmp, dns, tcp")
        sys.exit(1)


if __name__ == "__main__":
    main()
