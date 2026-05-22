# AI Ready Monitoring Platform

## Project Overview

AI Ready Monitoring Platform is a Python-based DevOps infrastructure monitoring and alerting system designed to monitor Linux servers using SSH automation, multithreading, logging, and Slack webhook integration.

This project simulates real-world infrastructure monitoring tools used in DevOps and Site Reliability Engineering (SRE) environments.

---

# Features

- Multi-server monitoring
- SSH automation using Paramiko
- CPU, Memory, and Disk monitoring
- Multithreading support
- Slack alert integration
- Centralized logging
- Health report generation
- Automated infrastructure monitoring

---

# Technologies Used

- Python
- Paramiko
- Requests
- Threading
- Linux
- Slack Webhooks
- Git & GitHub

---

# Project Structure

```bash
day7-ai-monitoring-platform/
│
├── monitor.py
├── servers.txt
├── requirements.txt
├── logs/
│   └── monitoring.log
├── reports/
│   └── health_report.txt
├── screenshots/
├── .gitignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/VKPACHAURI/ai-ready-monitoring-platform.git
```

## Move Into Project

```bash
cd ai-ready-monitoring-platform
```

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Slack Webhook

```bash
export SLACK_WEBHOOK_URL="YOUR_WEBHOOK_URL"
```

---

# Add Servers

Edit:

```bash
servers.txt
```

Add your server IPs or DNS names.

Example:

```text
172.31.33.105
```

---

# Run Project

```bash
python3 monitor.py
```

---

# Monitoring Features

This project monitors:

- System Uptime
- Memory Usage
- Disk Usage
- Infrastructure Health
- Multi-server Connectivity

---

# Example Commands Executed

```bash
uptime
free -m
df -h
```

---

# Logging

Logs are stored in:

```bash
logs/monitoring.log
```

---

# Reports

Generated reports stored in:

```bash
reports/health_report.txt
```

---

# Future Improvements

- Docker integration
- Kubernetes monitoring
- Grafana dashboards
- AI anomaly detection
- Email alerts
- AWS CloudWatch integration

---

# DevOps Concepts Used

- Infrastructure Monitoring
- SSH Automation
- Multithreading
- Logging
- Alerting
- DevOps Automation
- Environment Variables
- Linux Administration

---

# Author

vishesh 

Vishesh Pachauri

DevOps & Cloud Automation Engineer
