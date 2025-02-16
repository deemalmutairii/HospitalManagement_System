import requests
from utils.error_messages import SLACK_NOTIFICATION_FAILED

class SlackHelper:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_notification(self, message):
        """إرسال إشعار إلى Slack."""
        try:
            payload = {"text": message}
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            print("Notification sent successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send notification: {e}")
