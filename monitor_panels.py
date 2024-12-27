import requests
import schedule
import time
import os
from dotenv import load_dotenv

# Load API keys and sensitive data from .env file
load_dotenv()

PANEL_APIS = [
    {"name": "Panel 1", "api_key": os.getenv("PANEL1_API_KEY"), "url": "https://powerlikesprovider.com/api/v2"},
    # Add more panels as needed
]

SMS_API_URL = "https://api.yoursmsprovider.com/send"  # Replace with actual SMS API URL
SMS_API_KEY = os.getenv("SMS_API_KEY")
ALERT_THRESHOLD = 30  # Alert when balance is below this amount
RECIPIENTS = ["+1234567890"]  # List of phone numbers to notify

def check_balance():
    for panel in PANEL_APIS:
        try:
            response = requests.post(
                panel["url"],
                data={"key": panel["api_key"], "action": "balance"}
            )
            response_data = response.json()
            balance = float(response_data.get("balance", 0))
            
            print(f"Checked {panel['name']}: Balance is ${balance}")

            if balance < ALERT_THRESHOLD:
                send_sms(panel["name"], balance)
        except Exception as e:
            print(f"Error checking balance for {panel['name']}: {e}")

def send_sms(panel_name, balance):
    for recipient in RECIPIENTS:
        try:
            message = f"Alert: Balance on {panel_name} is ${balance:.2f}. Please refill immediately."
            response = requests.post(
                SMS_API_URL,
                headers={"Authorization": f"Bearer {SMS_API_KEY}"},
                data={"to": recipient, "message": message}
            )
            if response.status_code == 200:
                print(f"SMS sent to {recipient}: {message}")
            else:
                print(f"Failed to send SMS to {recipient}: {response.text}")
        except Exception as e:
            print(f"Error sending SMS: {e}")

# Schedule the balance check every 5 minutes
schedule.every(5).minutes.do(check_balance)

print("Monitoring started...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
