import requests

API_KEY = "14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"
WEBHOOK = "https://discord.com/api/webhooks/1514757021600055366/o67iC60ZiYFKETub2TqjRt8Cvikl78x_4N7QVmacte7kHs-AmvovGUVJAKha_PLBkiIe"

url = "https://prod.api-fortnite.com/api/v1/events/tracker"

headers = {
    "Authorization": API_KEY
}

r = requests.get(url, headers=headers)

msg = f"""
🏆 EVA Cup Test

Status:
{r.status_code}

Erste Daten:
{r.text[:500]}
"""

requests.post(
    WEBHOOK,
    json={
        "content": msg
    }
)

print("Gesendet")
