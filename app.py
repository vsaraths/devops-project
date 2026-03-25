import os
import time
import socket
import logging
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

VERSION = os.getenv('APP_VERSION', '1.0.0')
ENV = os.getenv("ENV", "dev")
PORT = int(os.getenv("PORT", 5000))

start_time = time.time()

@app.route('/')
def home():
    return jsonify({
        "service": "Arcadex Health service",
        "version": VERSION,
        "environment": ENV
    })

@app.route('/health')
def health():
    app.logger.info("Health check called")
    return jsonify({
        "status": "OK",
        "version": VERSION,
        "uptime": round(time.time() - start_time, 2),
        "hostname": socket.gethostname()
    })

@app.route('/ready')
def ready():
    return jsonify({"status": "ready"})

@app.route('/live')
def live():
    return jsonify({"status": "alive"})

@app.errorhandler(Exception)
def handle_error(e):
    app.logger.error(f"Error: {str(e)}")
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)
