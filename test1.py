import requests

# GeezSMS API details
headers = {"Authorization": f"Bearer {SMS_API_KEY}"}
SMS_API_URL = "https://api.geezsms.com/api/v1/send"
SMS_API_KEY = "lOKljLgwAovpMIm8K8ZgHRZ5oTHzBxLq"
TEST_PHONE_NUMBER = "+251945113048"  # Replace with your test number
TEST_MESSAGE = "This is a test SMS via GeezSMS API."

# Sending SMS
try:
    response = requests.post(
        SMS_API_URL,
        headers={
            "Authorization": f"Bearer {SMS_API_KEY}",  # Adjust if Bearer is not needed
            "Content-Type": "application/x-www-form-urlencoded"  # Typical for POST with form data
        },
        data={
            "to": TEST_PHONE_NUMBER,
            "message": TEST_MESSAGE
        }
    )

    # Output response
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS. Check the response text for details.")
except Exception as e:
    print(f"An error occurred: {e}")
