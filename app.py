from flask import Flask, render_template, request
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)
app.config["DEBUG"] = True

account_sid = os.getenv('ACC_SID')
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

def send_msg():
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14844168079',
                     to=''
                 )
    print("success============")
    # print(message.sid)

@app.route('/')
def index(): 
    # send_msg()
    return render_template('index.html')

@app.route('/level/1')
def level1(): 
    return render_template('level1.html')

@app.route('/success')
def success(): 
    return render_template('success.html')

@app.route('/fail')
def fail(): 
    return render_template('fail.html')


if __name__ == "__main__":
    app.run(debug=True, threaded = True)