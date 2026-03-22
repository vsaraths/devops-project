import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv('APP_VERSION', '1.0.0')
@app.route('/')
def home():
    return jsonify({"service": "Arcadex Health service",
                    "version": VERSION
                    })


@app.route('/health')
def health():
    return jsonify({"status": "OK", "version": VERSION})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

