import busio, digitalio, board, serial, json
import paho.mqtt.client as mqtt
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

TOPIC = 'hancooj/mcp'
CLIENT_ID = 'hancooj_raspi'
HOST = '10.43.1.15'

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, MCP.P0)

#print(chan.value, chan.voltage)

reading = chan.value / 63.875
voltage = reading * 5 / 1024
c = (voltage - 0.5) * 100
f = (c * 9 / 5) + 32
print(f'{f} degrees')

# print(voltage, chan.voltage)

with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
        line = ser.readline()
        ser_read = line.decode('utf-8')
        #print(reading, end='', flush=True)

print(f'Raspi Reading:   {reading}\nArduino Reading: {ser_read}')

client = mqtt.Client(client_id=CLIENT_ID, clean_session=False)
client.connect(HOST, 1883)
client.publish(TOPIC, payload=json.dumps(f), qos=0)
