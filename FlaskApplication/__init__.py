from flask import Flask
from flask import render_template
#import pymongo
app = Flask(__name__)

@app.route('/')
def home():
    text = { 'content': 'Welcome to learnmongo !' } 
    return render_template("home.html",
        title = 'Welcome',
        text = text)


app.debug = True
if __name__ == "__main__":
    app.run()
