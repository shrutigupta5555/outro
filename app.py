from flask import Flask, render_template, request, g
import os
import flask
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


def send_msg(mobile, hint):
    print(mobile, "=============================================")
    message = client.messages \
                .create(
                     body="your hint is: " +hint,
                     from_='+14844168079',
                     to=f"{mobile}"
                 )
    print("success============")
    print(message.sid)


def randlist(limit):
    lol = random.randint(0, 9)
    # global limit = limit + 1
    if lol in nums and limit < 30: 
        randlist(limit+1)
    else:
        nums.append(lol)
    # return nums

@app.route('/')
def index():
    nums.clear()
    for i in range(5):
        randlist(0)
    print(nums)
    return render_template('index.html')


@app.route('/phone', methods=['POST'])
def phone(): 
    p = request.values['phone']
    
    return ''

@app.route('/level/<levelnum>')
def level(levelnum): 
    levelnum = int(levelnum)
    return render_template('level.html', ques = data.questions[nums[levelnum-1]], ans = data.answers[nums[levelnum-1]], hint = data.hints[nums[levelnum-1]], url=data.img_url[nums[levelnum-1]], level = levelnum, next= levelnum+1, baamzi = nums[levelnum - 1])


@app.route('/hintlevel/<levelnum>/<baamzi>/<mobile>')
def levelhint(levelnum,baamzi, mobile):
    baamzi = int(baamzi)
    levelnum = int(levelnum)
    print(nums, levelnum - 1)
    send_msg(str(mobile),data.hints[baamzi])
    return render_template('level2.html', ques = data.questions[baamzi], ans = data.answers[baamzi], hint = data.hints[baamzi], url=data.img_url[baamzi], level = levelnum, next= levelnum+1)


@app.route('/success')
def success(): 
    return render_template('success.html')

@app.route('/fail')
def fail(): 
    return render_template('fail.html')

@app.route('/snap')
def snap():
    return render_template("snap.html")


if __name__ == "__main__":
    
    app.run(debug=True, threaded = True)