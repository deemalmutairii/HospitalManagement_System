from utils.slack_helper import SlackHelper
from utils.information_messages import SLACK_TEST_MESSAGE


def test_slack_notification():

    webhook_url = "https://hooks.slack.com/services/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"
    slack_helper = SlackHelper(webhook_url)


    slack_helper.send_notification(SLACK_TEST_MESSAGE)


if __name__ == "__main__":
    test_slack_notification()
