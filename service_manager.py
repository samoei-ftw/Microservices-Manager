# S O
# 09 Feb 2025
# Microservices Manager
# Handles microservices (start, stop, restart, status)

import subprocess
import signal
import json
import os

# Get services from config
with open("config.json") as f:
    SERVICES = json.load(f)
# Keep track of running processes    
processes={}

def start(service_name):
    """Start microservice by name"""
    if service_name in SERVICES and service_name not in processes:
        script_path = SERVICES[service_name]
        process = subprocess.Popen(["bash", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes[service_name] = process
        print(f"Started {service_name}")
    else:
        print(f"{service_name} is already running or does not exist.")

def stop(service_name):
    """Stop running a microservice"""
    if service_name in processes:
        process = processes[service_name]
        process.terminate()
        process.wait()
        del processes[service_name]
        print(f"Stopped {service_name}")
    else:
        print(f"{service_name} is not running")

def restart(service_name):
    stop(service_name)
    start(service_name)

def list_services():
    """List all running services"""
    if processes:
        print("Running services:")
        for name, process in processes.items():
            print(f"STARTING to run -> {name} (PID: {process.PID})\n")
    else:
        print("No services are currently running")

def shutdown():
    """Stop all services before exiting (the graceful way)"""
    for service in list(processes.keys()):
        stop(service)
    print("All services stopped. Shutting down...")

def start_all():
    for service in SERVICES:
        print(f"Starting service: {service}")
        start(service)