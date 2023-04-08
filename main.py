from helpers.api_helpers import sample_nexmo


def main():
    recipient_phone_number = input(
        "Enter the recipient's phone number (E.164 format): "
    )
    sample_nexmo(recipient_phone_number)


if __name__ == "__main__":
    main()
