import hashlib
import hmac
import json
import logging
import os
import re
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

from flask import Flask, jsonify, request


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MENUS = {
    "main": (
        "Welcome to the Indian Gas Company helpdesk.\n"
        "Reply with a number:\n"
        "1. Gas leakage\n"
        "2. Gas cylinder replacement\n"
        "3. Gas cylinder booking\n"
        "4. Gas cylinder delivery\n"
        "5. Gas cylinder cancellation\n"
        "6. Gas cylinder refund",
        {
            1: "Gas leakage",
            2: "Gas cylinder replacement",
            3: "Gas cylinder booking",
            4: "Gas cylinder delivery",
            5: "Gas cylinder cancellation",
            6: "Gas cylinder refund",
        },
    ),
    "leakage": (
        "Select the gas leakage issue:\n"
        "1. Leakage in kitchen\n"
        "2. Leakage in bathroom\n"
        "3. Pipeline leakage\n"
        "4. Leakage in the cylinder\n"
        "5. Leakage in the stove",
        {
            1: "Gas leakage in kitchen",
            2: "Gas leakage in bathroom",
            3: "Gas pipeline leakage",
            4: "Gas leakage in the cylinder",
            5: "Gas leakage in the stove",
        },
    ),
    "replacement": (
        "Select the cylinder replacement issue:\n"
        "1. Replacement in kitchen\n"
        "2. Replacement in bathroom\n"
        "3. Replacement of the pipeline\n"
        "4. Replacement of the stove\n"
        "5. Replacement due to an old cylinder",
        {
            1: "Gas cylinder replacement in kitchen",
            2: "Gas cylinder replacement in bathroom",
            3: "Gas cylinder replacement in the pipeline",
            4: "Gas cylinder replacement in the stove",
            5: "Gas cylinder replacement due to an old cylinder",
        },
    ),
    "booking": (
        "Select the booking payment method:\n"
        "1. Wallet\n"
        "2. Online payment\n"
        "3. Cash on delivery",
        {
            1: "Booking by wallet",
            2: "Booking by online payment",
            3: "Booking by cash on delivery",
        },
    ),
    "delivery": (
        "Select the delivery issue:\n"
        "1. Late delivery\n"
        "2. Delivery not received; booked 1 week ago\n"
        "3. Complaint about the delivery",
        {
            1: "Late delivery",
            2: "Delivery not received after booking 1 week ago",
            3: "Complaint about the delivery",
        },
    ),
    "cancellation": (
        "Select the cancellation reason:\n"
        "1. Delay in delivery of the cylinder\n"
        "2. Not needed now\n"
        "3. Booked by mistake\n"
        "4. Other",
        {
            1: "Cancellation due to delay in delivery of the cylinder",
            2: "Cancellation because it is not needed now",
            3: "Cancellation because it was booked by mistake",
            4: "Other cancellation reason",
        },
    ),
    "refund": (
        "Select the refund issue:\n"
        "1. Refund through online payment\n"
        "2. Refund for cash on delivery\n"
        "3. Refund not received",
        {
            1: "Refund through online payment",
            2: "Refund for cash on delivery",
            3: "Refund not received",
        },
    ),
}

NEXT_MENU = {
    1: "leakage",
    2: "replacement",
    3: "booking",
    4: "delivery",
    5: "cancellation",
    6: "refund",
}
START_WORDS = {"hi", "hello", "hey", "menu", "start", "restart"}
CONVERSATIONS: dict[str, str] = {}


def build_reply(sender: str, message: str) -> str:
    normalized_message = message.strip().casefold()
    if normalized_message in START_WORDS:
        CONVERSATIONS.pop(sender, None)
        return MENUS["main"][0]

    menu_name = CONVERSATIONS.get(sender, "main")
    prompt, options = MENUS[menu_name]
    if not normalized_message.isdecimal():
        return f"Please reply with one of the listed numbers.\n\n{prompt}"

    selection = int(normalized_message)
    if selection not in options:
        return f"That option is not available. Please choose a listed number.\n\n{prompt}"

    if menu_name == "main":
        CONVERSATIONS[sender] = NEXT_MENU[selection]
        return MENUS[NEXT_MENU[selection]][0]

    CONVERSATIONS.pop(sender, None)
    return (
        f"You selected: {options[selection]}.\n"
        "This demo does not submit bookings, cancellations, or refund requests. "
        "Please contact the gas company to complete your request.\n\n"
        "Send 'menu' to start again."
    )


def required_setting(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Required environment variable {name} is not set.")
    return value


def send_whatsapp_message(recipient: str, message: str) -> None:
    access_token = required_setting("WHATSAPP_ACCESS_TOKEN")
    phone_number_id = required_setting("WHATSAPP_PHONE_NUMBER_ID")
    api_version = required_setting("WHATSAPP_GRAPH_API_VERSION")
    if not re.fullmatch(r"v\d+\.\d+", api_version):
        raise RuntimeError("WHATSAPP_GRAPH_API_VERSION must look like vXX.X.")

    endpoint = (
        f"https://graph.facebook.com/{api_version}/"
        f"{quote(phone_number_id, safe='')}/messages"
    )
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {"preview_url": False, "body": message},
    }
    api_request = Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(api_request, timeout=15):
            logger.info("Sent WhatsApp reply successfully.")
    except HTTPError as error:
        logger.error("WhatsApp Cloud API returned HTTP %s", error.code)
        raise RuntimeError("WhatsApp Cloud API rejected the reply.") from error
    except URLError as error:
        logger.error("Could not reach WhatsApp Cloud API: %s", error.reason)
        raise RuntimeError("Could not reach WhatsApp Cloud API.") from error


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/webhook")
    def verify_webhook():
        try:
            verify_token = required_setting("WHATSAPP_VERIFY_TOKEN")
        except RuntimeError as error:
            logger.error("%s", error)
            return jsonify(error=str(error)), 500

        if (
            request.args.get("hub.mode") == "subscribe"
            and hmac.compare_digest(
                request.args.get("hub.verify_token", ""), verify_token
            )
        ):
            return request.args.get("hub.challenge", ""), 200
        return "Forbidden", 403

    @app.post("/webhook")
    def receive_webhook():
        try:
            app_secret = required_setting("WHATSAPP_APP_SECRET")
        except RuntimeError as error:
            logger.error("%s", error)
            return jsonify(error=str(error)), 500

        signature = request.headers.get("X-Hub-Signature-256", "")
        expected_signature = "sha256=" + hmac.new(
            app_secret.encode("utf-8"), request.get_data(), hashlib.sha256
        ).hexdigest()
        if not hmac.compare_digest(signature, expected_signature):
            return jsonify(error="Invalid webhook signature."), 401

        payload = request.get_json()
        if not isinstance(payload, dict):
            return jsonify(error="Expected a JSON object."), 400

        for entry in payload.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                for incoming_message in value.get("messages", []):
                    sender = incoming_message.get("from")
                    if not isinstance(sender, str) or not sender:
                        logger.warning("Ignoring WhatsApp message with no sender.")
                        continue

                    text_data = incoming_message.get("text", {})
                    message_text = (
                        text_data.get("body", "")
                        if incoming_message.get("type") == "text"
                        and isinstance(text_data, dict)
                        else ""
                    )
                    send_whatsapp_message(sender, build_reply(sender, message_text))

        return jsonify(status="received"), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
