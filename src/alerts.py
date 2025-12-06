# src/alerts.py
from twilio.rest import Client
import yaml

# Load config
with open("../config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

def send_sms(lat, lon):
    client = Client(config['TWILIO_SID'], config['TWILIO_TOKEN'])
    message = client.messages.create(
        body=f"SOS Alert! Location: https://maps.google.com/?q={lat},{lon}",
        from_=config['TWILIO_PHONE'],
        to=config['RECIPIENT_PHONE']
    )
    print(f"Alert sent: {message.sid}")