from flask import Flask
from flask import render_template

import pymongo

client=pymongo.MongoClient("mongodb://okaram:1qaz2wsx@widmore.mongohq.com:10010/okaram")

app = Flask(__name__)

@app.route('/')
def home():
    text = { 'content':  client.okaram.test.find_one()['name'] } 
    return render_template("home.html",
        title = 'Welcome',
        text = text)

@app.route('/')
def find():
    obj=client.okaram.test.find({'_id':request.args.get('id')});
    dict={'content': obj}
    return render_template("home.html",
        title = 'Welcome',
        text = dict)
    
app.debug = True
if __name__ == "__main__":
    app.run()
