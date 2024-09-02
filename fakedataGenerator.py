import requests
import random
import time
from datetime import datetime

url = 'http://localhost:1026/ngsi-ld/v1/entities/'
headers = {
    'Content-Type': 'application/json',
    'Link': '<http://context/user-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
}

def generate_battery_data():
    unique_id = f"urn:ngsi-ld:Battery:{datetime.now().strftime('%Y%m%d%H%M%S')}"
    return {
        "id": unique_id,
        "type": "BatteryCycle",
        "chargeLevel": {
            "type": "Property",
            "value": random.randint(0, 100),
            "unitCode": "P1"
        },
        "voltage": {
            "type": "Property",
            "value": round(random.uniform(3.0, 4.2), 2),
            "unitCode": "VLT"
        },
        "temperature": {
            "type": "Property",
            "value": random.randint(20, 40),
            "unitCode": "CEL"
        },
        "status": {
            "type": "Property",
            "value": random.choice(["charging", "discharging", "idle"])
        }
    }

def send_data_to_context_broker(data):
    print(f"Sending data: {data}")  # Debug: Print data being sent
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Response status code: {response.status_code}")  # Debug: Print status code
        if response.status_code == 201:
            print(f"Entity {data['id']} successfully created in the context broker.")
        else:
            print(f"Failed to create entity. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        data = generate_battery_data()
        send_data_to_context_broker(data)
        time.sleep(10)

if __name__ == "__main__":
    # Run the loop in a separate thread or process in Jupyter Notebook
    import threading
    threading.Thread(target=main).start()
