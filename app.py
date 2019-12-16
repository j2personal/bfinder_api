from flask import Flask
from twilio.rest import Client
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'bfinder_api'

@app.route('/send_notif')
def send_message():
    # Your Account SID from twilio.com/console
	account_sid = os.environ.get("TWILIO_SID")
	# Your Auth Token from twilio.com/console
	auth_token  = os.environ.get("TWILIO_AUTH_TOKEN")

	client = Client(account_sid, auth_token)

	message = client.messages.create(
	    to=os.environ.get("TO_NUMBER"), 
	    from_=os.environ.get("FROM_NUMBER"),
	    body="Notification Received!")

	return(message.sid)





