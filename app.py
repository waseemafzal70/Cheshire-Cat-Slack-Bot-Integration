import json
import asyncio
from flask import Flask, request, jsonify
import requests
import threading
from websockets.asyncio.client import connect

app = Flask(__name__)

SLACK_BOT_TOKEN = 'Paste_Your_SLACK_BOT_TOKEN_Here'
CHESHIRE_CAT_WS_URL = "ws://localhost:1865/ws"

# Function to send messages to Slack
def send_message_to_slack(channel_id, message):
    requests.post('https://slack.com/api/chat.postMessage', {
        'token': SLACK_BOT_TOKEN,
        'channel': channel_id,
        'text': message
    })

# Async function to interact with Cheshire Cat
async def send_to_cat_and_get_response(user_input):
    async with connect(CHESHIRE_CAT_WS_URL) as websocket:
        await websocket.send(json.dumps({"text": user_input}))
        
        # Process only the first valid response
        async for message in websocket:
            cat_response = json.loads(message)
            if cat_response["type"] == "chat":
                return cat_response["content"]

# Flask route to handle Slack events
@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json
    if 'challenge' in data:
        return jsonify({'challenge': data['challenge']})

    if 'event' in data and 'text' in data['event']:
        user_input = data['event']['text']
        channel_id = data['event']['channel']
        user_id = data['event']['user']
        
        if user_id == 'XXXXXXXXXX':  # Replace with actual bot user ID, Try auth.test to get your bot user ID
            return jsonify({"status": "ok"})

        print(f"Received message from Slack: {user_input}")

        # Process Slack message in a new thread to avoid blocking
        threading.Thread(
            target=process_slack_message, 
            args=(user_input, channel_id)
        ).start()

    return jsonify({"status": "ok"})

# Process Slack message
def process_slack_message(user_input, channel_id):
    response = asyncio.run(send_to_cat_and_get_response(user_input))
    print(f"Cheshire Cat Response: {response}")
    send_message_to_slack(channel_id, response)

if __name__ == '__main__':
    app.run(port=5000)

https://e842-37-226-57-170.ngrok-free.app/slack/events


Subscribe to bot events
Event Name	Description	Required Scope
message.channels
message.im

Subscribe to events on behalf of users
message.channels
message.im

OAuth & Permissions --> Bot Token Scopes
chat:write
chat:write.public
im:read
im:write


First run cheshoir cat on your system locally. Check if localhost:1865 is accessible. 
Install ngrok with command "choco install ngrok" or "pip install ngrok", after successful installation of ngrok run the following commands "ngrok config add-authtoken YOUR_AUTH_TOKEN_HERE", Next "ngrok http http://localhost:1865"