from flask import Flask, render_template, request
import os
from twilio.rest import Client
from dotenv import load_dotenv
import random
import data as data

load_dotenv()

nums = []
limit = 0
app = Flask(__name__)
app.config["DEBUG"] = True

account_sid = os.getenv('ACC_SID')
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

def send_msg():
    print()
    message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+14844168079',
                     to=''
                 )
    print("success============")
    print(message.sid)


def randlist():
    lol = random.randint(0, 9)
    # global limit = limit + 1
    if lol in nums:
        randlist()
    else:
        nums.append(lol)

@app.route('/')
def index(): 
    for i in range(5):
        randlist()
    # send_msg()
    print(nums)
    return render_template('index.html')

@app.route('/level/<levelnum>')
def level(levelnum): 
    levelnum = int(levelnum)
    return render_template('level.html', ques = data.questions[levelnum-1], ans = data.answers[levelnum-1], hint = data.hints[levelnum-1], url=data.img_url[levelnum-1], level = levelnum, next= levelnum+1)

@app.route('/success')
def success(): 
    return render_template('success.html')

@app.route('/fail')
def fail(): 
    return render_template('fail.html')


if __name__ == "__main__":
    app.run(debug=True, threaded = True)