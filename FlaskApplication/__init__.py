from flask import Flask
from flask import render_template

import pymongo

app = Flask(__name__)

@app.route('/')
def home():
    client=pymongo.MongoClient("mongodb://okaram:1qaz2wsx@widmore.mongohq.com:10010/okaram")
    text = { 'content':  client.okaram.test.find_one()['name'] } 
    return render_template("home.html",
        title = 'Welcome',
        text = text)


app.debug = True
if __name__ == "__main__":
    app.run()
