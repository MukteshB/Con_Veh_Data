from awscrt import mqtt
from awsiot import mqtt_connection_builder
import time
import json

# AWS IoT MQTT connection settings
ENDPOINT = "<your-endpoint>.iot.<region>.amazonaws.com"
CLIENT_ID = "mqtt-client"
PATH_TO_CERT = "path/to/certificate.pem.crt"
PATH_TO_KEY = "path/to/private.pem.key"
PATH_TO_ROOT = "path/to/AmazonRootCA1.pem"
TOPIC = "project/topic"

# Build the MQTT connection
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERT,
    pri_key_filepath=PATH_TO_KEY,
    ca_filepath=PATH_TO_ROOT,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=6
)

print(f"Connecting to {ENDPOINT} with client ID '{CLIENT_ID}'...")
connect_future = mqtt_connection.connect()
connect_future.result()
print("Connected!")

# Publish messages to the topic
try:
    for i in range(5):  # Send 5 messages as an example
        message = {
            "sensor": "temperature",
            "value": round(20 + i * 1.5, 2),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        mqtt_connection.publish(
            topic=TOPIC,
            payload=json.dumps(message),
            qos=mqtt.QoS.AT_LEAST_ONCE
        )
        print(f"Published: {json.dumps(message)} to topic {TOPIC}")
        time.sleep(2)  # Wait 2 seconds between messages
finally:
    print("Disconnecting...")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected!")
