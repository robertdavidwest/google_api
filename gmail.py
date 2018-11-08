import base64
import pandas as pd
from StringIO import StringIO

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from config import (
    SCOPES,
    GMAIL_CREDENTIALS_PATH,
    GMAIL_TOKEN_PATH
)

def get_gmail_service():
    store = file.Storage(GMAIL_TOKEN_PATH)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(GMAIL_CREDENTIALS_PATH, SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service.users()


def get_message_ids(service, search_query, snippet=False):
    """searching for an e-mail (Supports the same query format as the Gmail search box.
    For example, "from:someuser@example.com rfc822msgid:<somemsgid@example.com> is:unread")
    if snippet=True then a second parameter is returned with a list of e-mail snippets
    """
    result = service.messages().list(userId='me', q=search_query).execute()
    msg_ids = [r['id'] for r in result.get('messages')]
    if not snippet:
        return msg_ids

    snippets = [service.messages().get(userId='me', id=id_).execute()['snippet']
                for id_ in msg_ids]
    return msg_ids, snippets


def get_attachment_ids(messageId):
    msg = service.messages().get(userId='me', id=messageId).execute()
    attachmentIds = []
    for part in msg.get('payload').get('parts'):
        attachmentId = part.get('body').get('attachmentId')
        if attachmentId:
            attachmentIds.append(attachmentId)
    return attachmentIds


def attachmentId_to_dataframe(service, messageId, attachmentId):
    att = service.messages().attachments().get(
            userId='me', id=attachmentId, messageId=messageId).execute()
    data = att['data']
    str_csv  = base64.urlsafe_b64decode(data.encode('UTF-8'))
    df = pd.read_csv(StringIO(str_csv))
    return df


def get_csv_attachments(service, messageId):
    """Converts CSV attachments into pd.DataFrames
    """
    attachmentIds = get_attachment_ids(messageId)
    dfs = [attachmentId_to_dataframe(service, messageId, attId)
           for attId in attachmentIds]
    return dfs


if __name__ == '__main__':
    search_query = "test"
    service = get_gmail_service()
    message_id = get_message_ids(service, search_query)[0]
    df = get_csv_attachments(service, message_id)[0]
    print(df)
