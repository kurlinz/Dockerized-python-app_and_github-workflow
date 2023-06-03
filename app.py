from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!, this is a simple python flask app made for my interview assessment by Appsilon. Wish me luck!!!'

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
