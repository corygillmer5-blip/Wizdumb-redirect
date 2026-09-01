from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Wizdumb LLC Micro-Service Online"

@app.route('/gear/flowhood')
def redirect_flowhood():
    return "Redirect Active"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

