# Python Repo

This repository contains Python scripts for automation and data structures & algorithms (DSA) practice.

## Folder Structure

- **Automation/**: Scripts for automating system tasks.
	- `1_monitoring.py`: Monitors system CPU and memory usage using `psutil`.
- **DSA/**: Data Structures and Algorithms practice scripts.
	- `1_reverse_string.py`: Demonstrates multiple methods to reverse a string in Python.

## Setup

1. **Clone the repository**
	 ```bash
	 git clone <your-repo-url>
	 cd python_repo
	 ```
2. **Install dependencies** (for automation scripts)
	 ```bash
	 pip install psutil
	 ```

## Usage

### Automation: System Monitoring

Run the monitoring script to check CPU and memory usage:

```bash
python Automation/1_monitoring.py
```

**Output Example:**
```
CPU Usage: 15.0%, Memory Usage: 45.2%
```

### DSA: Reverse String

Run the reverse string script to see different methods for reversing a string:

```bash
python DSA/1_reverse_string.py
```

**Output Example:**
```
olleh
<reversed object at ...>
olleh
olleh
olleh
```
