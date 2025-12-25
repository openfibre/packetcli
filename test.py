#!/usr/bin/env python3
import sys
from src.icmp import main as icmp_main
from src.dns import main as dns_main
from src.tcp import main as tcp_main
from src.all import main as all_main


TOOLS = {
    "icmp": icmp_main,
    "dns": dns_main,
    "tcp": tcp_main,
    "all": all_main
}


def main():
    if len(sys.argv) < 2:
        print("PacketCLI - Network Testing Tools")
        print("Usage: python test.py <tool> [options]")
        print("\nAvailable Tools:")
        for tool in TOOLS:
            print(f"  {tool}")
        sys.exit(1)

    tool = sys.argv[1]

    if tool not in TOOLS:
        print(f"Error: Unknown tool '{tool}'")
        print(f"Available tools: {', '.join(TOOLS.keys())}")
        sys.exit(1)

    # Replace tool name with script name for argparse
    sys.argv[0] = f"python test.py {tool}"
    sys.argv.pop(1)
    TOOLS[tool]()


if __name__ == "__main__":
    main()
