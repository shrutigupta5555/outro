from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index(): 
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