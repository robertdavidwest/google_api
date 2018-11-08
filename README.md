# python-read-gmail

### Setup 

* Follow these instructions to allow python to access your gmail account:

https://developers.google.com/gmail/api/quickstart/python

### Usage 

I'm yet to find a satisfiying link to show how to use the API but luckily it is somewhat intuitive a user friendly. So here are the things I've figured out so far: 

* Use this function to get the gmail service and access to all messages (taken from the quickstart.py code):

```
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
GMAIL_CREDENTIALS_PATH = 'credentials.json'

def get_gmail_service():
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
    	flow = client.flow_from_clientsecrets(GMAIL_CREDENTIALS_PATH, SCOPES)
    	creds = tools.run_flow(flow, store)
	service = build('gmail', 'v1', http=creds.authorize(Http()))
	return service
```


* Once installed, the following link is useful for understaning how to use the API:

https://developers.google.com/api-client-library/python/