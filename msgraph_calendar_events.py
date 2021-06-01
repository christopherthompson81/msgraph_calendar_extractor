'''
# Outlook Calendar Extractor - Half Script

## Part 1

1. Go to https://developer.microsoft.com/en-us/graph/graph-explorer
2. Sign in to Graph Explorer
3. Execute "Sample Queries" -> "Outlook Calendar" -> GET all events in my calendar
    a. Satisfy the "consent" requirements of the API and run the query again.
4. Copy the "Access Token" generated using this query.

## Part 2

1. Replace the access token value with the one copied from Graph Explorer
2. Run the script and pipe the output into a file: i.e. python msgraph_calendar_events.py > out.json
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
