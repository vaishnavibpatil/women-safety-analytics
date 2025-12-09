# src/alerts.py
# ---------------------------------------------------------
# ALERTING MODULE
# ---------------------------------------------------------
# This file is responsible for sending emergency SMS alerts
# using the Twilio API. When the system detects an SOS
# gesture or a safety anomaly, this function is triggered.
# The SMS contains a Google Maps link with the user's
# latitude and longitude so the recipient can locate them.
# ---------------------------------------------------------

from twilio.rest import Client
import yaml

# ---------------------------------------------------------
# Load Twilio configuration (SID, token, phone numbers)
# from settings.yaml. These credentials are required to
# authenticate with Twilio and send SMS messages.
# ---------------------------------------------------------
with open("../config/settings.yaml", "r") as f:
    config = yaml.safe_load(f)

def send_sms(lat, lon):
    """
    Sends an SOS alert message using Twilio SMS service.

    Parameters:
        lat (float): Latitude of the user's location
        lon (float): Longitude of the user's location

    The SMS contains a clickable Google Maps link so the
    receiver can quickly track the sender’s location.
    """
    
    # Initialize Twilio client using account SID and auth token
    client = Client(config['TWILIO_SID'], config['TWILIO_TOKEN'])
    
    # Create and send the SMS message
    message = client.messages.create(
        body=f"SOS Alert! Location: https://maps.google.com/?q={lat},{lon}",
        from_=config['TWILIO_PHONE'],     # Twilio phone number
        to=config['RECIPIENT_PHONE']      # Emergency contact number
    )
    
    # Print message SID for debugging / confirmation
    print(f"Alert sent: {message.sid}")
