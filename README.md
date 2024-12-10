# Cheshire Cat Slack Bot Integration
This repository provides a Flask-based integration to connect Slack with Cheshire Cat through WebSockets. The bot listens to messages in Slack, sends them to Cheshire Cat, and relays the responses back to the Slack channel.

## Prerequisites
**Cheshire Cat:** Ensure Cheshire Cat is running locally and accessible at http://localhost:1865.

**Ngrok:** Install and configure Ngrok to expose the local server.
## Installing Ngrok
**Using Chocolatey or Pip:**

`choco install ngrok`

`pip install ngrok`

## Setup Instructions
### 1. Start Cheshire Cat Locally
Run Cheshire Cat and verify that it is accessible at `http://localhost:1865`.

### 2. Configure Ngrok
After installing Ngrok, configure and expose your flask local server:

`ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE`

`ngrok http http://localhost:5000`

You will see output similar to:
`https://xxxxxxxxxxxxx.ngrok-free.app -> 127.0.0.1:5000`

Save the `https://` link; it will be used in Slack bot settings.

### 3. Create and Configure a Slack Bot
**Create a Slack Bot:**
Go to Slack's App Management Page and create a new app.

**Allow Required Permissions:**
Bot User OAuth Token Scopes:

`chat:write`

`chat:write.public`

`im:read`

`im:write`

`Subscribe to Bot Events:`

`message.channels`

`message.im`

Subscribe to Events on Behalf of Users:

`message.channels`

`message.im`

**Enable Event Subscriptions:**

Enable events in the Event Subscriptions section and paste the Ngrok link in the following format:

`https://xxxxxxxxxxxxx.ngrok-free.app/slack/events`

### 4. Update the Script
**Replace tokens in the Script:**
Slack Bot Token:
Replace `'Paste_Your_SLACK_BOT_TOKEN_Here'` with your bot's OAuth token.

Bot User ID:
Replace `'XXXXXXXXXX'` with your bot's user ID (found via auth.test API).

Start the Script:
`python app.py`

### 5. Test Your Bot
Start chatting with your bot in Slack.
Check responses in Slack and verify logs in the terminal (e.g., VS Code).
