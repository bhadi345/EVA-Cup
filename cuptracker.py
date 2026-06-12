import requests
from datetime import datetime

API_KEY="14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"
WEBHOOK="https://discord.com/api/webhooks/1514757021600055366/o67iC60ZiYFKETub2TqjRt8Cvikl78x_4N7QVmacte7kHs-AmvovGUVJAKha_PLBkiIe"

url="https://prod.api-fortnite.com/api/v1/events/global"

headers={
    "x-api-key":API_KEY
}

r=requests.get(url,headers=headers)

events=r.json()

msg="@everyone\n\n🏆 **Nächste EU Cups**\n\n"

count=0

for event in events:

    if "EU" in event.get("regions", {}):

        for cup in event["regions"]["EU"]:

            name=event.get("titleLine1","Cup")

            start=cup["beginTime"]

            dt=datetime.fromisoformat(
                start.replace("Z","+00:00")
            )

            zeit=dt.strftime("%d.%m • %H:%M UTC")

            msg+=f"🎯 {name}\n🕒 {zeit}\n\n"

            count+=1

            if count>=5:
                break

    if count>=5:
        break

msg+="💙 EVA Esports"

requests.post(
WEBHOOK,
json={
"content":msg
}
)

print("Gesendet")
