import os
import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello!'

@app.route('/hello')
def hello():
    phrase = random.choice([
        "Hello!",
        "Hi there!",
        "Greetings!",
        "Salutations!",
        "Howdy!",
        "Hey!",
        "What's up?",
        "Good day!",
        "Yo!",
        "Hiya!"
    ])
    return phrase

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)