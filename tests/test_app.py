import sys
import os
# Додаємо корінь проекту до шляху Python для імпорту app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from Integrated System!" in response.data

# Додайте інші тести, включаючи інтеграційні з моком симулятора АЗ
def test_status_mocked():
     client = app.test_client()
     # Тут можна використати mocking для hw_client, якщо він використовується
     response = client.get('/status')
     assert response.status_code == 200
     json_data = response.get_json()
     assert json_data["software_status"] == "OK"
     assert "hardware_status" in json_data