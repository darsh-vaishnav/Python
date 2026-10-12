# WhatsApp gas-help chatbot

This sample connects the gas-help menus to Meta's WhatsApp Cloud API. It can
guide a person through the leakage, replacement, booking, delivery,
cancellation, and refund options. It only confirms the selected issue; it does
not create bookings, cancel orders, submit support tickets, or process refunds.

## Run locally

1. Install Python dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

2. In the Meta app's WhatsApp API setup, get the access token and phone number
   ID. Set the app secret and choose a webhook verification token of your own.
   Set these values in PowerShell (keep real credentials private):

   ```powershell
   $env:WHATSAPP_ACCESS_TOKEN = "your access token"
   $env:WHATSAPP_PHONE_NUMBER_ID = "your phone number ID"
   $env:WHATSAPP_APP_SECRET = "your Meta app secret"
   $env:WHATSAPP_VERIFY_TOKEN = "your chosen verification token"
   $env:WHATSAPP_GRAPH_API_VERSION = "vXX.X"
   ```

   Replace `vXX.X` with a currently supported Graph API version shown in your
   Meta app.

3. Start the local server:

   ```powershell
   py whatsapp_bot.py
   ```

4. Meta must be able to reach the webhook over public HTTPS. For local
   development, expose port 5000 using a trusted HTTPS tunnel, then configure
   the resulting URL with `/webhook` in your Meta app. Use the same verification
   token as `WHATSAPP_VERIFY_TOKEN` and subscribe to the `messages` webhook
   field.

For deployment, use a production WSGI server and store credentials in the
hosting provider's secret/environment-variable settings. Do not expose Flask's
development server directly to the internet. Conversation progress is kept in
memory, so this sample is intended for a single process and loses unfinished
conversations when restarted.

Run the tests from this directory with:

```powershell
py -m unittest -v
```
