from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/level/1')
def level(): 
    return render_template('game.html')


if __name__ == "__main__":
    app.run(debug=True, threaded = True)