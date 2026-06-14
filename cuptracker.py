import requests

API_KEY = "14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"

url = "https://prod.api-fortnite.com/api/v1/events/global"

headers = {
    "x-api-key": API_KEY
}

try:
    r = requests.get(url, headers=headers, timeout=30)

    print("STATUS CODE:")
    print(r.status_code)

    print("\nHEADERS:")
    print(r.headers)

    print("\nANTWORT:")
    print(r.text[:2000])

except Exception as e:
    print("FEHLER:")
    print(e)
