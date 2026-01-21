from datetime import datetime, timedelta
import json
import os
import requests

logs_directory = "logs"
pulse_file = "pulse_data.json"
  
def initialize_storage():
    if not os.path.exists(logs_directory):
        os.mkdir(logs_directory)
    if not os.path.exists(pulse_file):
        with open(pulse_file, "w") as file:
            json.dump([], file)

def load_services():
    with open(pulse_file, 'r') as file:
        services = json.load(file)
    return services

def save_services(services):
    with open(pulse_file, 'w') as file:
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
        duration = response.elapsed.total_seconds() * 1000
        if response.status_code in range(200, 300):
            service['status'] = 'UP'
            service['status_code'] = response.status_code
            service['response_time'] = duration

        elif response.status_code in range(300, 500):
            service['status'] = 'UNSTABLE'
            service['status_code'] = response.status_code
            service['response_time'] = duration

        elif response.status_code in range(500, 600):
            service['status'] = 'DOWN'
            service['status_code'] = response.status_code
            service['response_time'] = duration
        
        service['last_checked'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out.")
        service['status'] = 'DOWN'
        service['status_code'] = None
        service['response_time'] = None
        service['last_checked'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    except requests.RequestException:
        print("Connection error:")
        service['status'] = 'DOWN'
        service['status_code'] = None
        service['response_time'] = None
        service['last_checked'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        write_service_log(service)

def write_service_log(service):
    log_file = os.path.join(logs_directory, f"{service['name'].lower()}.json")

    log_entry = {
        "timestamp": service['last_checked'],
        "status": service['status'],
        "status_code": service['status_code'],
        "response_time": service['response_time']
    }

    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            logs = json.load(file)
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, 'w') as file:
        json.dump(logs, file, indent=2)

initialize_storage()
main_menu()

while True:
    services = load_services()
    for service in services:

        last_checked_time = datetime.strptime(service['last_checked'],"%Y-%m-%d %H:%M:%S")

        next_check_time = last_checked_time + timedelta(seconds=service['interval'])  
        if last_checked_time >= next_check_time:
            check_service(service)
    save_services(services)