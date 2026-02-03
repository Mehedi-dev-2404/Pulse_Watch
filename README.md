# Pulse Watch

## Overview

Pulse Watch is a lightweight, real-time service monitoring solution designed to track the availability and performance of web services through periodic health checks. Built with Python, it provides automated monitoring capabilities with persistent storage and comprehensive logging, making it suitable for development environments, small-scale production monitoring, and educational purposes.

## Core Features

### Service Monitoring
- Continuous health checks for multiple web services
- Configurable check intervals per service
- HTTP status code detection and categorization
- Response time measurement in milliseconds
- Automatic status classification (UP, UNSTABLE, DOWN)

### Data Management
- JSON-based persistent storage for service configuration
- Per-service historical log files
- Automatic log directory initialization
- Atomic file operations for data integrity

### Error Handling
- Graceful timeout management (10-second default)
- Connection failure detection and logging
- Service status tracking across failure states
- Non-blocking error recovery

### User Interface
- Interactive command-line interface
- Service registration and removal
- Real-time service status viewing
- Input validation and error feedback

## Technical Architecture

### Project Structure

```
Pulse_Watch/
├── pulse_watch.py       # Main application logic
├── pulse_data.json      # Service configuration database
├── logs/                # Historical monitoring data
│   ├── google.json
│   ├── github.json
│   └── brokenservice.json
└── README.md
```

### Service Data Model

Each monitored service maintains the following properties:

```json
{
  "name": "Google",
  "url": "https://www.google.com",
  "interval": 10,
  "status": "UP",
  "last_checked": "2026-01-21 14:10:05",
  "response_time": 120.4,
  "status_code": 200
}
```

**Field Descriptions:**
- `name`: Unique identifier for the service
- `url`: Target endpoint for health checks
- `interval`: Check frequency in seconds
- `status`: Current health status (UP, UNSTABLE, DOWN, UNKNOWN)
- `last_checked`: Timestamp of most recent check
- `response_time`: HTTP response duration in milliseconds
- `status_code`: HTTP status code from last check

### Status Classification

| HTTP Status Code | Service Status |
|-----------------|----------------|
| 200-299         | UP             |
| 300-499         | UNSTABLE       |
| 500-599         | DOWN           |
| Connection Error| DOWN           |
| Timeout         | DOWN           |

### Log File Structure

Each service generates individual log files with timestamped entries:

```json
{
  "timestamp": "2026-01-21 14:10:05",
  "status": "UP",
  "status_code": 200,
  "response_time": 120.4
}
```

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. Clone or download the project:
```bash
git clone <repository-url>
cd Pulse_Watch
```

2. Install required dependencies:
```bash
pip install requests
```

3. Initialize the application:
```bash
python pulse_watch.py
```

The application will automatically create necessary directories and configuration files on first run.

## Usage

### Starting the Application

Run the main script to launch the interactive interface:

```bash
python pulse_watch.py
```

### Command-Line Interface

```
=============================
 Pulse Watch - Service Monitor
==============================
1. Add Service
2. Remove Service
3. View Services
4. Exit
```

### Adding a Service

1. Select option 1 from the main menu
2. Enter service name (must be unique)
3. Provide full URL including protocol (http:// or https://)
4. Specify check interval in seconds

Example:
```
Enter service name: GitHub
Enter service URL: https://www.github.com
Enter check interval (in seconds): 15
Service 'GitHub' added successfully.
```

### Removing a Service

1. Select option 2 from the main menu
2. Enter the exact name of the service to remove
3. Service and its logs will be removed from active monitoring

### Viewing Services

Select option 3 to display all registered services with their current status, last check time, and configuration details.

## Implementation Details

### Monitoring Loop

The application operates on a continuous monitoring cycle:

1. Load service configuration from `pulse_data.json`
2. Calculate next check time based on last check timestamp and interval
3. Execute HTTP GET request to service URL
4. Parse response for status code and response time
5. Update service status based on HTTP status code
6. Persist results to service-specific log file
7. Save updated configuration
8. Sleep for 1 second before next iteration

### Asynchronous Operation

The monitoring loop runs independently after the main menu, allowing services to be checked automatically in the background while maintaining interactive capabilities for service management.

### Data Persistence

All service configurations and logs are stored in JSON format for human readability and easy integration with other tools. The application implements atomic write operations to prevent data corruption during concurrent operations.

## Use Cases

- Development environment health monitoring
- API endpoint availability tracking
- Website uptime monitoring
- Educational demonstration of service monitoring concepts
- Prototyping for larger monitoring systems
- Testing HTTP endpoint reliability

## Technical Concepts Demonstrated

- Scheduled task execution
- HTTP client implementation
- File-based persistent storage
- JSON data serialization
- Error handling and exception management
- Command-line interface design
- Time-based event scheduling
- Status code interpretation
- Performance measurement

## System Requirements

- Operating System: Cross-platform (Windows, macOS, Linux)
- Python Version: 3.9+
- Network: Internet connectivity required for external service monitoring
- Storage: Minimal (logs scale with check frequency and retention)
- Memory: Low footprint (suitable for resource-constrained environments)

## Limitations

- Single-threaded execution (sequential service checking)
- No notification system for status changes
- Manual configuration (no web interface)
- No authentication support for protected endpoints
- Limited to HTTP/HTTPS protocols
- No data aggregation or analytics capabilities

## Future Enhancements

### Planned Features

**Multi-threaded Monitoring**
- Concurrent service checks using threading or async/await
- Improved performance for monitoring multiple services
- Reduced latency between check cycles

**Notification System**
- Email alerts for service status changes
- Webhook integration for external notification services
- SMS notifications via third-party APIs
- Configurable alert thresholds and cooldown periods

**Web Dashboard**
- Real-time service status visualization
- Historical uptime graphs and charts
- REST API for programmatic access
- Mobile-responsive interface

**Advanced Analytics**
- Uptime percentage calculations
- Response time trend analysis
- Service comparison metrics
- Exportable reports (PDF, CSV)

**Enhanced Security**
- Authentication support for protected endpoints
- SSL certificate validation options
- API key management for secured services
- Encrypted storage for sensitive credentials

**Database Integration**
- SQLite backend for improved query performance
- PostgreSQL support for enterprise deployments
- Time-series database integration for metrics
- Data retention and archival policies

**Configuration Improvements**
- YAML-based configuration files
- Environment variable support
- Configuration validation and schema enforcement
- Import/export of service configurations

**Extended Protocol Support**
- TCP port monitoring
- ICMP ping checks
- DNS resolution verification
- Custom protocol handlers

## Contributing

This project is designed as a learning tool and portfolio demonstration. Contributions, suggestions, and feedback are welcome to improve functionality and code quality.

## License

This project is available for educational and portfolio purposes.

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
