# python-read-gmail

### Setup 

* Follow these instructions to allow python to access your gmail account:

https://developers.google.com/gmail/api/quickstart/python

### Usage 

API Documentation is here: https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/

* Use this function to get the gmail service and access to all messages (taken from the `quickstart.py` code):

```
import base64
import pandas as pd
from StringIO import StringIO

from googleapiclient.discovery import build
from httplib2 import Http
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
    return service.users()

# searching for an e-mail (Supports the same query format as the Gmail search box.
# For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com> is:unread")
q = "looking for this text"
result = service.messages().list(userId='me', q=q).execute()
msg_ids = [r['id'] for r in result.get('messages')]
for id_ in msg_ids:
    msg = service.messages().get(userId='me', id=id_).execute()
    print(msg['snippet'])


# Converting a CSV attachment from an e-mail into a pd.DataFrame

messageId = 'XYZ'
msg = service.messages().get(userId='me', id=messageId).execute()
attachmentIds = []
for part in msg.get('payload').get('parts'):
    attachmentId = part.get('body').get('attachmentId')
    if attachmentId:
        attachmentIds.append(attachmentId)


attachmentId = "ABC"
att = service.messages().attachments().get(
    userId='me', id=attachmentId, messageId=messageId).execute()
data = att['data']
str_csv  = base64.urlsafe_b64decode(data.encode('UTF-8'))
df = pd.read_csv(StringIO(str_csv))

```
