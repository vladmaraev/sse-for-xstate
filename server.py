from flask import Flask
from flask_sse import sse
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(sse, url_prefix='/stream')
app.config["REDIS_URL"] = "redis://localhost"
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/send')
def send_message():
    sse.publish({"message": "Hello!"}, type='caramba')
    return "Message sent!"
