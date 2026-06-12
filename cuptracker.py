import requests

API_KEY = "14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"

url = "https://prod.api-fortnite.com/api/v1/events/tracker"

headers = {
    "Authorization": API_KEY
}

r = requests.get(url, headers=headers)

print(r.status_code)
print(r.text[:2000])
