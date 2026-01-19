import json
import os

pulse_file = "pulse_data.json"

try:
    with open(pulse_file, "r") as file:
        pulse_data = file.read()
        print("Pulse data loaded successfully.")
except FileNotFoundError:
    with open(pulse_file, "w") as file:
        file.write("[]")
    print("Pulse data file not found. Created a new one.")
  
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