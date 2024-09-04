import json
import random
import time

def generate_sensor_data(sensor_id):
    data = {
        "sensor_id": sensor_id,
        "timestamp": time.time(),
        "temperature": round(random.uniform(15.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "unit": "Celsius"
    }
    return json.dumps(data)

if __name__ == "__main__":
    sensor_id = "sensor-001"
    for _ in range(10):
        sensor_data = generate_sensor_data(sensor_id)
        print(sensor_data)
        time.sleep(1)
import json
import random
import time

def generate_sensor_data(sensor_id):
    data = {
        "sensor_id": sensor_id,
        "timestamp": time.time(),
        "temperature": round(random.uniform(15.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "unit": "Celsius"
    }
    return json.dumps(data)

if __name__ == "__main__":
    sensor_id = "sensor-001"
    for _ in range(10):
        sensor_data = generate_sensor_data(sensor_id)
        print(sensor_data)
        time.sleep(1)

