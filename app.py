from flask import Flask
from twilio.rest import Client
import os

app = Flask(__name__)

def send_message(msg):
    # Your Account SID from twilio.com/console
    account_sid = os.environ.get("TWILIO_SID")
    # Your Auth Token from twilio.com/console
    auth_token  = os.environ.get("TWILIO_AUTH_TOKEN")

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=os.environ.get("TO_NUMBER"), 
        from_=os.environ.get("FROM_NUMBER"),
        body=msg)

    return(message.sid)


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'bfinder_api'

@app.route('/send_vib')
def send_vib():
    send_message("Incoming Notification!")
    return("Vib Sent")

# @app.route('/request_juber', methods=["POST"])
# def request_juber():
#     request.form.get("")
#     send_message("")
#     return("Vib Sent")





