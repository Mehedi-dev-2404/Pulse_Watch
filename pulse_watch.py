import json
import os
import requests

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
        json.dump(services, file, indent=2)

def service_exists(services, name):
    for service in services:
        if service['name'] == name:
            return True
    return False

def main_menu():
    while True:
        print("")
        print("=============================")
        print(" Pulse Watch - Service Monitor")
        print("==============================")
        print("1. Add Service")
        print("2. Remove Service")
        print("3. View Services")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            add_service()
        elif choice == '2':
            remove_service()
        elif choice == '3':
            view_services()
        elif choice == '4':
            print("Exiting Pulse Watch. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def add_service():
    services = load_services()

    name = input("Enter service name: ")

    if service_exists(services, name):
        print(f"Service '{name}' already exists.")
        return
    
    url = input("Enter service URL: ")
    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL. Please enter a valid URL starting with http:// or https://")
        return

    try:
        interval = int(input("Enter check interval (in seconds): "))
        if interval <= 0:
            print("Interval must be a positive integer.")
            raise ValueError
    except ValueError:
        print("Invalid interval. Please enter a positive integer.")
        return
    
    new_service = {
        "name": name,
        "url": url,
        "interval": interval,
        "status": "UNKNOWN",
        "last_checked": None,
        "response_time" : None,
        "status_code": None
    }

    services.append(new_service)
    save_services(services)
    print(f"Service '{name}' added successfully.")

def remove_service():
    services = load_services()
    remove_name = input("Enter the name of the service to remove: ")

    updated_sevice = [service for service in services if service['name'] != remove_name]

    if len(updated_sevice) == len(services):
        print(f"No service found with the name '{remove_name}'.")
        return
    
    save_services(updated_sevice)
    print(f"Service '{remove_name}' removed.")

def view_services():
    data = load_services()
    if data:
        print("Registered Services:")
        print("-"* 20)
        for service in data:
            print(f"Name: {service['name']} | URL: {service['url']} | Interval: {service['interval']}s | Status: {service['status']} | Last Checked: {service['last_checked']}")
    else:
        print("No services registered.")
        
def check_service(service):
    url = service['url']
    try:
        response = requests.get(url, timeout=10)
        duration = str(response.elapsed.total_seconds() * 1000)
        
        if response.status_code in range(200, 300):
            service['status'] = 'UP'
            service['status_code'] = response.status_code
            service['response_time'] = duration
        else:
            service['status'] = 'DOWN'
            service['status_code'] = response.status_code
            service['response_time'] = duration

    except TimeoutError:
        print(f"Request to {url} timed out.")
        service['status'] = 'DOWN'


initialize_storage()
main_menu()