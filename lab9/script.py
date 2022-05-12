import serial, json, sys
import paho.mqtt.client as mqtt

TOPIC = 'hancooj/temps'
CLIENT_ID = 'hancooj_raspi'
HOST = '10.43.1.15'

client = mqtt.Client(client_id=CLIENT_ID, clean_session=False)
client.connect(HOST, 1883)

try:
    while True:
        with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
            line = ser.readline()

        reading = line.decode('utf-8')
        print(reading, end='', flush=True)

        file_string = f'sensor:arduino,temp:{reading}'
        with open('temps.csv', 'a') as f:
            f.write(file_string)

        json_payload = {'sensor': 'arduino', 'temperature': reading.replace('\n', '')}
        client.publish(TOPIC, payload=json.dumps(json_payload), qos=0)

except KeyboardInterrupt:
    print('ending transmission')
    sys.exit()
