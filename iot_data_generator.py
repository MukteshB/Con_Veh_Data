import random
import time
import json

def generate_sensor_data():
    sensors = ['temperature', 'humidity', 'pressure', 'vibration']
    data = {
        "sensor": random.choice(sensors),
        "value": round(random.uniform(10.0, 100.0), 2),
        "unit": "Celsius" if "temperature" else "%",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return data

def main():
    print("IoT Data Generator Running...")
    while True:
        data = generate_sensor_data()
        print(json.dumps(data))
        time.sleep(2)  # Generate data every 2 seconds

if __name__ == "__main__":
    main()
