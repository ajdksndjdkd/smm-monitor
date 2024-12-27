import requests

# Replace with your actual SMS API details
SMS_API_URL = "https://api.geezsms.com/api/v1/send"  # Update if needed
SMS_API_KEY = "WpFv4fHoAYtTMSv0kF9XOEE2QWUQugnM"  # Replace with your SMS API key
TEST_PHONE_NUMBER = "+251945113048"  # Replace with a test phone number
TEST_MESSAGE = "This is a test SMS from your monitoring script."

try:
    # Send a test SMS
    response = requests.post(
        SMS_API_URL,
        headers={"Authorization": f"Bearer {SMS_API_KEY}"},
        data={"to": TEST_PHONE_NUMBER, "message": TEST_MESSAGE}
    )
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS. Check the response above for details.")
except Exception as e:
    print(f"An error occurred: {e}")
