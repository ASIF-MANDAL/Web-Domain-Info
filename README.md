# Domain Info Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Python script to generate an Excel file containing domain information such as **Domain Name**, **IP Address**, **IP Class**, and **Reply** (reachability status) for a list of websites.

---

## Features

- Fetches IP addresses for a list of domains.
- Determines the IP class (A, B, C, D, or E).
- Checks if the domain is reachable (Reply status).
- Generates an Excel file (`domain_info.xlsx`) with the results.
- Supports thousands of domains using multi-threading for faster processing.

---

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries: `pandas`, `requests`

You can install the required libraries using:

```bash
pip install pandas requests
