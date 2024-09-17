from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong", "time": time.time()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34289)