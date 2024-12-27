import requests

SMS_API_URL = " https://api.geezsms.com/api/v1/send"  # Replace with actual SMS API URL
SMS_API_KEY = "lOKljLgwAovpMIm8K8ZgHRZ5oTHzBxLq"  # Replace with your SMS API key
TEST_PHONE_NUMBER = "+251945113048"  # Replace with your test phone number
TEST_MESSAGE = "This is a test SMS from the SMM monitor amir."

response = requests.post(
    SMS_API_URL,
    headers={"Authorization": f"Bearer {SMS_API_KEY}"},
    data={
        "to": TEST_PHONE_NUMBER,
        "message": TEST_MESSAGE
    }
)

print(response.status_code, response.text)
