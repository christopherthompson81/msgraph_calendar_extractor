'''
Outlook Calendar Extractor
'''
import json
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
URL = "https://graph.microsoft.com/v1.0/me/events"

entries = list()
headers = {
    "Authorization": "Bearer " + ACCESS_TOKEN
}
current_url = URL
while(current_url):
    response = requests.get(current_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        entries = entries + data["value"]
        current_url = data.get('@odata.nextLink', False)
    else:
        print("Non-OK Status Received:", response.status_code, response.text, sep=" ")
        exit()
print(json.dumps(entries, indent=4))
