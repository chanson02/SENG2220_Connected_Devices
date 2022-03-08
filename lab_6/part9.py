import requests

response = requests.get("http://10.43.2.9:1880/get_temps_cooper").json()
count = len(response)
# Print the 10 most recent values
for i in range(count-10, count):
    print(response[i])
