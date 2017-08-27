#!/usr/bin/python3

from flask import Flask, current_app
app = Flask(__name__)
print("one")

@app.route('/')
def index():
    return current_app.send_static_file('index.html')
    print("why")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
