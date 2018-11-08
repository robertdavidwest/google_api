# python-read-gmail

### Setup 

* Set up the conda envrionment "google-api":

        $ conda env create -f environment.yml 

* Follow these instructions to allow python to access your gmail account (skip the past about installing python packages, thats already taken care of in the conda envionment"):

    https://developers.google.com/gmail/api/quickstart/python

* After the set up you will download a file called `credentials.json`. Be sure to update the variable `GMAIL_CREDENTIALS_PATH` path to this file in `config.py`. Also update the `GMAIL_TOKEN_PATH` to be a file called `*-token.json` in the same directory

    e.g:
    ```
    config.py 

    GMAIL_CREDENTIALS_PATH = "credentials.json"
    GMAIL_TOKEN_PATH = "token.json"
    ```

### Usage 

API Documentation is here: https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/

* Use this function to get the gmail service and access to all messages (taken from the `quickstart.py` code):

```
from gmail import *
search_query = "test"

# read a snippet of text from all e-mails that contains the str 'test'
service = get_gmail_service()
_, snippets = get_message_ids(service, search_query, snippet=True)
for sn in snippets:
    print(sn)

# convert a csv file from an e-mail into a pd.DataFrame
# if that email contains the word 'test'
message_id = get_message_ids(service, search_query)[0]
df = get_csv_attachments(service, message_id)[0]
print(df)
```

