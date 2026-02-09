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

**Learning Topic:**

Check Palindrom - If we are reading form left to right or from right to left it must be same 
                ex :- 121 -> palindrom,  nitin -> palindrom
				   :- 123-> not palindrome, abcd -> not palindrome


check Armstrong no - An Armstrong number (or narcissistic number) is a positive integer equal to the sum of its own digits each raised to the power of the total number of 	digits. For 
				ex :- 153 is an Armstrong number because \(1^{3}+5^{3}+3^{3}=153\), 
				   :- 1634 is one because \(1^{4}+6^{4}+3^{4}+4^{4}=1634\). 

Learning about hasing - We have to deal with list/tupple/dict for hasing (number hashing and char hashing)

Learning about Recursion - Implemneted head and tail recursion basic

Learned about fibonacchi series

Learned about shorting selection sort, bubble sort (Pratice done), need to do hands on insertion sort.

Learned about sorting merge sort, 