import paramiko
import threading
import requests
import json
import logging
import os

# Create folders automatically
os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename="logs/monitoring.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Slack Webhook from environment variable
webhook_url = os.getenv("SLACK_WEBHOOK_URL")

# SSH details
username = "ubuntu"
pem_file = "paramiko.pem"

# Commands to execute
commands = [
    "uptime",
    "free -m",
    "df -h"
]

# Read server list
with open("servers.txt") as file:
    servers = file.read().splitlines()

# Report file
report_file = "reports/health_report.txt"

def monitor_server(server):

    try:

        print(f"\nConnecting to {server}")

        ssh = paramiko.SSHClient()

        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            hostname=server,
            username=username,
            key_filename=pem_file
        )

        with open(report_file, "a") as report:

            report.write(f"\n===== SERVER: {server} =====\n")

            for command in commands:

                stdin, stdout, stderr = ssh.exec_command(command)

                output = stdout.read().decode()

                print(f"\nCommand: {command}")
                print(output)

                report.write(f"\nCommand: {command}\n")
                report.write(output)

        ssh.close()

        logging.info(f"{server} monitored successfully")

    except Exception as e:

        print(f"Error connecting to {server}: {e}")

        logging.error(f"{server}: {e}")

        # Slack alert
        if webhook_url:

            message = {
                "text": f"🚨 Monitoring Failed for Server: {server}\nError: {e}"
            }

            requests.post(
                webhook_url,
                data=json.dumps(message),
                headers={"Content-Type": "application/json"}
            )

# Multithreading
threads = []

for server in servers:

    thread = threading.Thread(
        target=monitor_server,
        args=(server,)
    )

    thread.start()

    threads.append(thread)

for thread in threads:

    thread.join()

print("\n✅ Monitoring Completed")



