from flask import Flask, jsonify
import os
import logging

print("--- app.py SCRIPT STARTED ---")
app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(name)s:%(message)s', force=True)

@app.route('/')
def hello():
    logging.info("Root endpoint accessed")
    return "Hello from Integrated System!"

@app.route('/status')
def status():
    try:
        hw_status = {"component": "sensor A", "value": 12.5, "status": "OK"} 
        logging.info(f"Hardware status requested: {hw_status}")
        return jsonify({"software_status": "OK", "hardware_status": hw_status})
    except Exception as e:
        logging.error(f"Error getting hardware status: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    print("--- BEFORE app.run() ---")

    app.run(host='0.0.0.0', port=5000)
