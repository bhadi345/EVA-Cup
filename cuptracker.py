import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1514757021600055366/o67iC60ZiYFKETub2TqjRt8Cvikl78x_4N7QVmacte7kHs-AmvovGUVJAKha_PLBkiIe"

text = """
@everyone 🏆 Nächste EU Cups

🎯 Solo Victory Cup
🕒 19:00 Uhr

🎯 Duo Cash Cup
🕒 20:00 Uhr
"""

requests.post(
    WEBHOOK_URL,
    json={"content": text}
)
