import json
import os

pulse_file = "pulse_data.json"
  
def initialize_storage():
    if not os.path.exists(pulse_file):
        with open(pulse_file, "w") as file:
            json.dump([], file)

def load_services():
    with open('pulse_data.json', 'r') as file:
        services = json.load(file)
    return services

def save_services(services):
    with open('pulse_data.json', 'w') as file:
        json.dump(services, file)

def service_exists(services, name):
    for service in services:
        if service['name'] == name:
            return True
    return False

initialize_storage()
services = load_services()