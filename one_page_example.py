from flask import Flask
app = Flask(__name__)
@app.route('/')
def land():
    return {
        "you've officially landed" : "welcome to baby's first flask app!"
    }
@app.route('/home')
def home():
    return {
        "home sweet home!" : "there's no place like hiraeth!"
    }
@app.route('/students')
def students():
    return {
        "hey y'all, " : "this one's for all of you reprobates!"
    }
@app.route('/test')
def test():
    return {
        "test" : "this is a test"
    }
app.run()