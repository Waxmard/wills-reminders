# helpers/api_helpers.py

"""
This module contains the functions related to interacting with the Nexmo API, such as sending text messages.
"""
import vonage

from config.settings import (
    FROM_PHONE_NUMBER,
    NEXMO_API_KEY,
    NEXMO_API_SECRET,
    TO_PHONE_NUMBER,
)


def sample_nexmo():
    client = vonage.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": FROM_PHONE_NUMBER,
            "to": TO_PHONE_NUMBER,
            "text": "A text message sent using the Nexmo SMS API",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
