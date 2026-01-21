# Pulse_Watch

Pulse Watch

Pulse Watch is a command-line service monitoring tool written in Python.
It periodically checks the availability and performance of registered web services, records their status, and maintains historical logs for later analysis.

⸻

Overview

Pulse Watch allows users to register services with custom check intervals. Each service is monitored continuously, with results persisted to disk and logged per service.

The tool is designed for clarity, reliability, and educational value, demonstrating core backend concepts such as scheduling, persistence, error handling, and structured logging.

⸻

Features
	•	Interval-based service health checks
	•	HTTP status code monitoring
	•	Response time measurement
	•	Persistent storage using JSON
	•	Per-service historical log files
	•	Graceful handling of timeouts and connection failures
	•	Interactive command-line interface

⸻

Project Structure

Pulse_Watch/
├── pulse_watch.py
├── pulse_data.json
└── logs/
    ├── google.json
    ├── github.json
    └── example_service.json


⸻

How It Works
	1.	Services are stored in pulse_data.json
	2.	Each service defines:
	•	A target URL
	•	A check interval (in seconds)
	3.	A monitoring loop:
	•	Determines when a service is due for checking
	•	Sends an HTTP request
	•	Updates service status, response time, and timestamp
	•	Appends results to a per-service log file inside logs/

⸻

Service Data Model

{
  "name": "Google",
  "url": "https://www.google.com",
  "interval": 10,
  "status": "UP",
  "last_checked": "2026-01-21 14:10:05",
  "response_time": 120.4,
  "status_code": 200
}


⸻

Log File Format

Each service has its own log file stored under the logs/ directory.

{
  "timestamp": "2026-01-21 14:10:05",
  "status": "UP",
  "status_code": 200,
  "response_time": 120.4
}

Log entries are appended to preserve historical monitoring data.

⸻

Command-Line Interface

1. Add Service
2. Remove Service
3. View Services
4. Exit


⸻

Installation and Usage

Requirements
	•	Python 3.9 or later
	•	requests library

Install Dependencies

pip install requests

Run the Application

python pulse_watch.py


⸻

Error Handling

Pulse Watch is designed to fail safely and continue running. It handles:
	•	Network timeouts
	•	Invalid or unreachable URLs
	•	Invalid user input
	•	Duplicate service registrations

Failures are recorded without interrupting the monitoring loop.

⸻

Design Decisions
	•	JSON-based storage for transparency and ease of inspection
	•	Polling-based scheduler for simplicity and clarity
	•	Per-service log files to isolate monitoring history
	•	Defensive defaults to prevent runtime exceptions

⸻

Possible Enhancements
	•	Uptime percentage calculations
	•	Aggregated response-time statistics
	•	Alerting via email, Slack, or webhooks
	•	Asynchronous or multi-threaded monitoring
	•	Export logs to CSV or database storage

⸻

Learning Outcomes

This project demonstrates practical experience with:
	•	Python scripting and CLI tools
	•	Time-based scheduling logic
	•	Persistent data management
	•	Structured logging
	•	Defensive programming
	•	Backend system design fundamentals

⸻

License

This project is released under the MIT License.
