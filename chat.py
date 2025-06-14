from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

messages = []
msg_id = 1

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def post_message():
    global msg_id
    data = request.json
    msg = {
        "id": msg_id,
        "user": data.get("user", "You"),
        "text": data.get("text", ""),
        "timestamp": int(time.time())
    }
    messages.append(msg)
    msg_id += 1
    return jsonify(msg), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
