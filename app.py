from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return f"Hello, World did you know it is {datetime.now()}!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
