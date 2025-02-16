
from utils.slack_helper import SlackHelper
from utils.information_messages import DATABASE_CONNECTED

def test_slack_notification():
    """Test sending a Slack notification."""
    webhook_url = "https://hooks.slack.com/services/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"
    slack_helper = SlackHelper(webhook_url)

    try:
        slack_helper.send_notification(DATABASE_CONNECTED)
        print("Slack notification test passed.")
    except Exception as e:
        print(f"Slack notification test failed: {e}")

if __name__ == "__main__":
    test_slack_notification()
