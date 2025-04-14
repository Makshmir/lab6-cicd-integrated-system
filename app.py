from flask import Flask, jsonify
import os
import logging
# Припустимо, є бібліотека для взаємодії з симулятором АЗ
# from hw_simulator_client import HWSimulatorClient
print("--- app.py SCRIPT STARTED ---") # <--- ДОДАЙТЕ ЦЕ
app = Flask(__name__)

# Цей рядок налаштовує КОРЕНЕВИЙ логер Python
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(name)s:%(message)s', force=True)
# Додано force=True про всяк випадок, щоб гарантувати застосування конфігурації

# Приклад підключення до симулятора АЗ (адреса з docker-compose)
# hw_sim_address = os.environ.get("HW_SIMULATOR_ADDRESS", "http://az_simulator:8080")
# hw_client = HWSimulatorClient(hw_sim_address)

@app.route('/')
def hello():
    # Використовуємо logging замість app.logger
    logging.info("Root endpoint accessed")
    return "Hello from Integrated System!"

@app.route('/status')
def status():
    try:
        # Приклад отримання статусу від симулятора АЗ
        # hw_status = hw_client.get_status()
        hw_status = {"component": "sensor A", "value": 12.5, "status": "OK"} # Заглушка
        # Використовуємо logging замість app.logger
        logging.info(f"Hardware status requested: {hw_status}")
        return jsonify({"software_status": "OK", "hardware_status": hw_status})
    except Exception as e:
        # Використовуємо logging замість app.logger
        logging.error(f"Error getting hardware status: {e}")
        return jsonify({"error": str(e)}), 500

# Додайте ендпоінт для метрик Prometheus (використовуючи prometheus_client)
# from prometheus_client import make_wsgi_app, Counter
# metrics_app = make_wsgi_app()
# c = Counter('my_failures', 'Description of counter')
# @app.route('/metrics')
# def metrics():
#     return metrics_app

if __name__ == '__main__':
    print("--- BEFORE app.run() ---") # <--- ДОДАЙТЕ ЦЕ
    # Важливо: Не запускайте в режимі debug=True для цього тесту,
    # бо він має власний спосіб перезавантаження та логування.
    app.run(host='0.0.0.0', port=5000)