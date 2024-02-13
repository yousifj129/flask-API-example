from flask import Flask
from chatbot import Chatbot


c = Chatbot()

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>hello</p>"

@app.route("/chat/<text>")
def chat(text):
    response = c.chat(text)
    return response

if __name__ == "__main__":
    c.loadData("flask-API-example/dialo.csv")
    app.run()