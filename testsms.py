import requests

SMS_API_URL = "https://api.yoursmsprovider.com/send"  # Replace with actual SMS API URL
SMS_API_KEY = "your-sms-api-key"  # Replace with your SMS API key
TEST_PHONE_NUMBER = "+1234567890"  # Replace with your test phone number
TEST_MESSAGE = "This is a test SMS from the SMM monitor."

response = requests.post(
    SMS_API_URL,
    headers={"Authorization": f"Bearer {SMS_API_KEY}"},
    data={
        "to": TEST_PHONE_NUMBER,
        "message": TEST_MESSAGE
    }
)

print(response.status_code, response.text)
