# Microservices Manager
## Project Description
This project automates the management of four .sh scripts that start and stop Docker-based microservices.
It provides a CLI interface to start, stop, restart, and check the status of services dynamically.

## Feature List
Start a Service \
Stop a Service \
Start all Services \
Restart a Service \
Check Service Status \
List All Running Services \
Graceful Exit (Stop All Services) \
Logging \
Config File Support 

## How to Use:
eg: Start all services in config file
1. Add a config.json file with key-values for service names and their file paths. eg: {"service1":"dir/./run_local_docker.sh", "service2":"dir/./run_local_docker2.sh"} 
2. python3 main.py start all 


eg: Start 'service1' 
1. Add a config.json file with key-values for service names and their file paths. eg: {"service1":"dir/./run_local_docker.sh"} 
2. python3 main.py start service1 

## File structure
| ----  `config.json` -> config file mapping service names to .sh scripts \
| ----  `main.py` -> main script with CLI logic \
| ----  `service_manager.py` -> core functions \
| ----  `logs/` -> service logs (if opt to save logs to dir) \
| ----  `scripts/` -> .sh files for starting services \
| ----  `README.md` -> documentation 
