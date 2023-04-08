from flask import Flask, request

app = Flask(__name__)


@app.route("/delivery-receipt", methods=["POST"])
def delivery_receipt():
    receipt = request.form.to_dict()
    status = receipt["status"]
    message_id = receipt["messageId"]

    if status == "delivered":
        print(f"Message with ID {message_id} was delivered.")
    else:
        print(f"Message with ID {message_id} failed with status: {status}")

    return "", 204


if __name__ == "__main__":
    app.run(port=8080)
