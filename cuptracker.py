import requests
from datetime import datetime
from zoneinfo import ZoneInfo

API_KEY="14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"
WEBHOOK="https://discord.com/api/webhooks/1514757021600055366/o67iC60ZiYFKETub2TqjRt8Cvikl78x_4N7QVmacte7kHs-AmvovGUVJAKha_PLBkiIe"

url="https://prod.api-fortnite.com/api/v1/events/global"

headers={
    "x-api-key":API_KEY
}

r=requests.get(url,headers=headers)

events=r.json()

msg="@everyone\n\n🏆 **Nächste EU Cups**\n\n"

seen=set()
count=0

for event in events:

    if "EU" not in event.get("regions",{}):
        continue

    name=event.get("titleLine1","Cup")

    for cup in event["regions"]["EU"]:

        start=cup["beginTime"]

        key=(name,start)

        if key in seen:
            continue

        seen.add(key)

        dt=(
            datetime
            .fromisoformat(start.replace("Z","+00:00"))
            .astimezone(
                ZoneInfo("Europe/Berlin")
            )
        )

        zeit=dt.strftime("%d.%m • %H:%M")

        msg+=(
            f"🎯 {name}\n"
            f"🕒 {zeit} Uhr\n\n"
        )

        count+=1

        if count>=5:
            break

    if count>=5:
        break

msg+="📍 Region: EU\n💙 EVA Esports"

requests.post(
    WEBHOOK,
    json={
        "content":msg
    }
)

print("Gesendet")
