import requests

url = "https://fortnitetracker.com/events.ics?region=EU"

r = requests.get(url)

print(r.text[:500])
