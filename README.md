# wills-reminders
I want to solve the problem of Will's crippling ADHD disallowing him to remember to be quiet, to smoke weed, to workout, to bully kaelan,... and many other things he needs a bit of help to accomplish.

Wills-Reminders is a Python project that sends SMS messages using the Nexmo API. The project includes a Flask app to handle delivery receipts, providing more accurate information about the delivery status of messages.

## Requirements

- Python 3.11
- A Nexmo account with API key and secret
- Flask
- ngrok (for exposing the local webhook server)

## Installation

1. Clone the repository.

    ```bash
    git clone https://github.com/yourusername/wills-reminders.git
    cd wills-reminders
    ```

2. Set up a virtual environment and install the required packages.

    ```bash
    python -m venv venv
    source venv/bin/activate # For Windows, use "venv\Scripts\activate"
    pip install -r requirements.txt
    ```

3. Create a `.env.development` file in the project root directory with your Nexmo API credentials and phone numbers. Replace the placeholders with your actual values.

    ```.env
    NEXMO_API_KEY=your_api_key
    NEXMO_API_SECRET=your_api_secret
    FROM_PHONE_NUMBER=nexmo_provided_phone_number
    ```

## Usage

1. Start the Flask app by running:

    ```bash
    python receiver/webhook.py
    ```

    This will start the webhook server that listens for delivery receipts.

2. In another terminal window, run `ngrok` to expose your webhook server to the internet. Make sure to use the provided public URL from `ngrok` in your Nexmo account settings.

    ```bash
    ngrok http 8080 # For Windows, use "ngrok.exe http 8080"
    ```

3. Run `main.py` to send a message.

    ```
    python main.py
    ```

    Enter the recipient's phone number when prompted, and the message will be sent.

4. Check the terminal where the Flask app is running to see the delivery status of your messages.

## How it works

This project uses the Nexmo API to send SMS messages. The `sample_nexmo` function in `helpers/api_helpers.py` is responsible for sending messages. It takes a recipient phone number as an argument and sends a predefined message to the specified number.

To provide more accurate information about the delivery status of messages, the project includes a Flask app that listens for delivery receipts from Nexmo. When a message is sent, Nexmo sends a delivery receipt to the webhook endpoint configured in the Nexmo account settings. The Flask app receives the delivery receipt and prints the delivery status in the terminal.

To expose the local webhook server to the internet, the project uses `ngrok`. This allows Nexmo to send delivery receipts to the webhook even when the webhook server is running on a local machine.
