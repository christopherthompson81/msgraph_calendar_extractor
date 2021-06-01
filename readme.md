# Outlook Calendar Extractor

## Part 1

1. Go to https://developer.microsoft.com/en-us/graph/graph-explorer
2. Sign in to Graph Explorer
3. Execute "Sample Queries" -> "Outlook Calendar" -> GET all events in my calendar
    a. Satisfy the "consent" requirements of the API and run the query again.
4. Copy the "Access Token" generated using this query.

## Part 2

1. Replace the access token value with the one copied from Graph Explorer
2. Run the script and pipe the output into a file: i.e. python msgraph_calendar_events.py > out.json
