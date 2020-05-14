
#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return "Hello World!"

#start the server
if __name__ == "__main__":
    app.run()