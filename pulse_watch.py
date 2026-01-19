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

def main_menu():
    while True:
        print("=============================")
        print(" Pulse Watch - Service Monitor")
        print("==============================")
        print("1. Add Service")
        print("2. Remove Services")
        print("3. View Services")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_service()
        elif choice == '2':
            remove_services()
        elif choice == '3':
            view_services()
        elif choice == '4':
            print("Exiting Pulse Watch. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    

initialize_storage()
services = load_services()