import requests
from utils.ErrorMessages import SLACK_NOTIFICATION_FAILED

class SlackHelper:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_notification(self, message):
        """Send a notification to Slack using a webhook URL."""
        try:
            payload = {"text": message}
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            print("Notification sent successfully.")
        except requests.exceptions.RequestException as e:
            print(SLACK_NOTIFICATION_FAILED.format(response.status_code))
