import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

API_KEY="14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"
WEBHOOK="https://discord.com/api/webhooks/1514757021600055366/o67iC60ZiYFKETub2TqjRt8Cvikl78x_4N7QVmacte7kHs-AmvovGUVJAKha_PLBkiIe"

url="https://prod.api-fortnite.com/api/v1/events/global"

headers={
    "x-api-key": API_KEY
}

r=requests.get(url,headers=headers)

events=r.json()

berlin=ZoneInfo("Europe/Berlin")
now=datetime.now(timezone.utc)

cups=[]

for event in events:

    if "EU" not in event.get("regions",{}):
        continue

    name=event.get("titleLine1","Cup")

    for cup in event["regions"]["EU"]:

        try:

            start=datetime.fromisoformat(
                cup["beginTime"].replace(
                    "Z",
                    "+00:00"
                )
            )

            if start < now:
                continue

            cups.append({
                "name":name,
                "time":start
            })

        except:
            continue


cups=sorted(
    cups,
    key=lambda x:x["time"]
)

seen=set()
final=[]

for cup in cups:

    key=(
        cup["name"],
        cup["time"].strftime("%Y-%m-%d")
    )

    if key in seen:
        continue

    seen.add(key)
    final.append(cup)

    if len(final)>=5:
        break


msg="@everyone\n\n🏆 **Nächste EU Cups**\n\n"

for cup in final:

    zeit=(
        cup["time"]
        .astimezone(berlin)
        .strftime("%d.%m • %H:%M")
    )

    msg+=(
        f"🎯 {cup['name']}\n"
        f"🕒 {zeit} Uhr\n\n"
    )

msg+="📍 Region: EU\n💙 EVA Esports"

requests.post(
    WEBHOOK,
    json={
        "content":msg
    }
)

print("Gesendet")
