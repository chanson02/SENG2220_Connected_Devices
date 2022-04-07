import requests
data = requests.get('http://10.32.2.9:1880/get_temps_cooper').json()
[print(f"Location: {data[i]['location']}  |  Sensor: {data[i]['sensor']}  |  Temperature: {data[i]['temp']}") for ndx in range(5)]
