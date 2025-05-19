import requests

# Example of hardcoded secret (Bearer should flag this)
API_KEY = "sk_test_51Habc1234567890abcdef"

def send_data(data):
    # Example of insecure HTTP request (Bearer should flag this)
    url = "http://example.com/api"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code)

send_data({"email": "user@example.com", "ssn": "123-45-6789"})
