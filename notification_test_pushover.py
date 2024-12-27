import requests


def send_pushover_notification(message, title="Notification"):
    api_url = "https://api.pushover.net/1/messages.json"
    data = {
        "token": "anavkp6xtan4rx7i3crxvjw98mwe9y",
        "user": "u7bvz94odhxpn8xv7gmb2hfiprzuhr",
        "message": message,
        "title": title,
    }
    
    response = requests.post(api_url, data=data)
    
    if response.status_code == 200:
        print("Notification sent successfully!")
    else:
        print(f"Failed to send notification. Error: {response.text}")

# Example usage
send_pushover_notification("This is a test message from Python!", title="Hello from Python")
