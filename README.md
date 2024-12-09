# Con_Veh_Data
this is connected vehicle Data for project
# IoT Data Generator

This repository simulates IoT sensor data for tutorials and testing.

## Features
- Randomly generates sensor data (e.g., temperature, humidity).
- Outputs data in JSON format every 2 seconds.

## Prerequisites
- AWS account with an EC2 instance.
- Python 3.x installed.

## How to Clone and Run
1. SSH into your EC2 instance:
   ```bash
   ssh -i "your-key.pem" ec2-user@<EC2-public-IP>

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/IoT-Data-Generator.git
cd IoT-Data-Generator
Run the script:

bash
Copy code
python3 iot_data_generator.py
Sample Output
json
Copy code
{"sensor": "temperature", "value": 72.34, "unit": "Celsius", "timestamp": "2024-12-09 10:30
