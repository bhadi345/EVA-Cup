import requests

url = "https://www.fortnite.com/competitive/?region=EU"

r = requests.get(url)

print(r.text[:1000])
