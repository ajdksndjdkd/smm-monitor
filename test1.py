import requests

# Replace with your actual API key and test phone number
SMS_API_URL = "https://api.geezsms.com/api/v1/send"
SMS_API_KEY = "WpFv4fHoAYtTMSv0kF9XOEE2QWUQugnM"
TEST_PHONE_NUMBER = "+251945113048"  # Replace with a valid phone number
TEST_MESSAGE = "This is a test SMS from your monitoring script."

try:
    # Send SMS
    response = requests.post(
        SMS_API_URL,
        headers={
            "Authorization": f"Bearer {SMS_API_KEY}",  # Adjust if "Bearer" is not needed
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data={
            "to": TEST_PHONE_NUMBER,
            "message": TEST_MESSAGE
        }
    )

    # Debug logs
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS. Check the response text above for details.")
except Exception as e:
    print(f"An error occurred: {e}")
