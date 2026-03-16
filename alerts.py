import requests

# Replace with your Slack webhook URL
SLACK_WEBHOOK = ""


def send_alert(message):

    if not SLACK_WEBHOOK:
        return

    payload = {
        "text": message
    }

    try:
        requests.post(SLACK_WEBHOOK, json=payload)
    except Exception as e:
        print("Slack alert failed:", e)
        