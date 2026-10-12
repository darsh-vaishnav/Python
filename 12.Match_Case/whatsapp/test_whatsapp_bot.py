import hashlib
import hmac
import json
import os
import unittest
from unittest.mock import patch

import whatsapp_bot


class WhatsAppBotTests(unittest.TestCase):
    def setUp(self):
        whatsapp_bot.CONVERSATIONS.clear()
        self.app = whatsapp_bot.create_app()
        self.client = self.app.test_client()
        self.environment = patch.dict(
            os.environ,
            {
                "WHATSAPP_VERIFY_TOKEN": "verify-test",
                "WHATSAPP_APP_SECRET": "app-secret-test",
            },
        )
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def test_booking_delivery_cancellation_and_refund_menus(self):
        cases = [
            ("3", 1, "Booking by wallet", "1. Wallet"),
            ("3", 2, "Booking by online payment", "2. Online payment"),
            ("3", 3, "Booking by cash on delivery", "3. Cash on delivery"),
            ("4", 1, "Late delivery", "1. Late delivery"),
            (
                "4",
                2,
                "Delivery not received after booking 1 week ago",
                "2. Delivery not received; booked 1 week ago",
            ),
            ("4", 3, "Complaint about the delivery", "3. Complaint"),
            (
                "5",
                1,
                "Cancellation due to delay in delivery of the cylinder",
                "1. Delay in delivery",
            ),
            (
                "5",
                2,
                "Cancellation because it is not needed now",
                "2. Not needed now",
            ),
            (
                "5",
                3,
                "Cancellation because it was booked by mistake",
                "3. Booked by mistake",
            ),
            ("5", 4, "Other cancellation reason", "4. Other"),
            (
                "6",
                1,
                "Refund through online payment",
                "1. Refund through online payment",
            ),
            (
                "6",
                2,
                "Refund for cash on delivery",
                "2. Refund for cash on delivery",
            ),
            ("6", 3, "Refund not received", "3. Refund not received"),
        ]
        for index, (category, option, confirmation, menu_option) in enumerate(cases):
            sender = f"sender-{index}"
            prompt = whatsapp_bot.build_reply(sender, category)
            self.assertIn(menu_option, prompt)
            reply = whatsapp_bot.build_reply(sender, str(option))
            self.assertIn(confirmation, reply)
            self.assertIn("does not submit", reply)

    def test_root_selection_routes_to_expected_menu(self):
        self.assertIn("Gas cylinder booking", whatsapp_bot.build_reply("a", "3"))
        self.assertIn("Gas cylinder delivery", whatsapp_bot.build_reply("b", "4"))
        self.assertIn(
            "Gas cylinder cancellation", whatsapp_bot.build_reply("c", "5")
        )
        self.assertIn("Gas cylinder refund", whatsapp_bot.build_reply("d", "6"))

    def test_invalid_selection_keeps_current_menu(self):
        whatsapp_bot.build_reply("sender", "3")
        response = whatsapp_bot.build_reply("sender", "9")
        self.assertIn("That option is not available", response)
        self.assertIn("3. Cash on delivery", response)

    def test_webhook_verification(self):
        response = self.client.get(
            "/webhook",
            query_string={
                "hub.mode": "subscribe",
                "hub.verify_token": "verify-test",
                "hub.challenge": "challenge-value",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "challenge-value")

    def test_message_webhook_checks_signature_and_sends_reply(self):
        payload = {
            "entry": [
                {
                    "changes": [
                        {
                            "value": {
                                "messages": [
                                    {
                                        "from": "1234567890",
                                        "type": "text",
                                        "text": {"body": "3"},
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
        raw_payload = json.dumps(payload).encode("utf-8")
        signature = "sha256=" + hmac.new(
            b"app-secret-test", raw_payload, hashlib.sha256
        ).hexdigest()
        with patch("whatsapp_bot.send_whatsapp_message") as send_message:
            response = self.client.post(
                "/webhook",
                data=raw_payload,
                content_type="application/json",
                headers={"X-Hub-Signature-256": signature},
            )
        self.assertEqual(response.status_code, 200)
        send_message.assert_called_once()
        self.assertEqual(send_message.call_args.args[0], "1234567890")
        self.assertIn("Select the booking payment method", send_message.call_args.args[1])

    def test_message_webhook_rejects_bad_signature(self):
        response = self.client.post(
            "/webhook",
            data="{}",
            content_type="application/json",
            headers={"X-Hub-Signature-256": "sha256=invalid"},
        )
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
