import requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

API_KEY="14eb41dafca37dc846edbcf65aa3678fbee1268ec4aa8956f58c8de83b5b3c66"
WEBHOOK="https://discord.com/api/webhooks/1514757021600055366/o67iC60ZiYFKETub2TqjRt8Cvikl78x_4N7QVmacte7kHs-AmvovGUVJAKha_PLBkiIe"

url="https://prod.api-fortnite.com/api/v1/events/global"

headers={
    "x-api-key":API_KEY
}

r=requests.get(url,headers=headers)

events=r.json()

berlin=ZoneInfo("Europe/Berlin")
now=datetime.now(timezone.utc)

cups=[]

for event in events:

    if "EU" not in event.get("regions",{}):
        continue

    name=event.get(
        "titleLine1",
        "Cup"
    )

    for cup in event["regions"]["EU"]:

        try:

            start=datetime.fromisoformat(
                cup["beginTime"]
                .replace("Z","+00:00")
            )

            end=datetime.fromisoformat(
                cup["endTime"]
                .replace("Z","+00:00")
            )

            if end < now:
                continue

            cups.append({
                "name":name,
                "start":start,
                "end":end
            })

        except:
            pass


cups=sorted(
    cups,
    key=lambda x:x["start"]
)

seen=set()
final=[]

for cup in cups:

    key=(
        cup["name"],
        cup["start"]
    )

    if key in seen:
        continue

    seen.add(key)

    final.append(cup)

    if len(final)>=6:
        break


msg="@everyone\n\n🏆 **Heute & Nächste EU Cups**\n\n"

for cup in final:

    start=(
        cup["start"]
        .astimezone(berlin)
        .strftime("%H:%M")
    )

    end=(
        cup["end"]
        .astimezone(berlin)
        .strftime("%H:%M")
    )

    tag=(
        cup["start"]
        .astimezone(berlin)
        .strftime("%d.%m")
    )

    msg+=(
        f"🎯 {cup['name']}\n"
        f"🕒 {tag} • {start} - {end}\n\n"
    )

msg+="📍 Region: EU\n💙 EVA Esports"

requests.post(
WEBHOOK,
json={
"content":msg
}
)

print("Gesendet")
