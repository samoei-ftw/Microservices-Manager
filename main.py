# 09 Feb 2025
# Microservices Manager CLI 
# Handles user input and calls service functions

import argparse
from service_manager import start, stop, restart, shutdown, list_services


parser = argparse.ArgumentParser(description="Manage Docker microservices")
parser.add_argument("command", choices=[
    "start",
    "stop",
    "restart",
    "status",
    "exit"
], help=["Action to perform"])
parser.add_argument("service", nargs="?", help="Service name (optional for 'status' and 'exit')")
args = parser.parse_args()

if args.command == "start" and args.service:
    start(args.service)
elif args.command == "stop" and args.service:
    stop(args.service)
elif args.command == "restart" and args.service:
    restart(args.service)
elif args.command == "status":
    list_services()
elif args.command == "exit":
    shutdown()
else:
    print("Invalid command or missing service name.")