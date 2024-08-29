import requests
import urllib3

# Disable the SSL warning (useful for testing; enable SSL verification in production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# APIC details
apic_url = "https://172.16.100.75"
username = "vector"
password = "Vector@123"

# Define the login URL
login_url = f"{apic_url}/api/aaaLogin.json"

# Prepare login payload
payload = {
    "aaaUser": {
        "attributes": {
            "name": username,
            "pwd": password
        }
    }
}

# Send POST request to login
response = requests.post(login_url, json=payload, verify=False)

# Check if the request was successful
if response.status_code == 200:
    login_data = response.json()
    token = login_data['imdata'][0]['aaaLogin']['attributes']['token']
    print("API Token:", token)
else:
    print("Failed to get API token:", response.text)
