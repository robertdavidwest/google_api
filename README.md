# python-read-gmail

### Setup 

* Set up the conda envrionment "google-api":

        $ conda env create -f environment.yml 

* Follow these instructions to allow python to access your gmail account (skip the past about installing python packages, thats already taken care of in the conda envionment"):

    https://developers.google.com/gmail/api/quickstart/python

* After the set up you will download a file called `credentials.json`. Be sure to update the variable `GMAIL_CREDENTIALS_PATH` path to this file in `example.py`. Also update the `GMAIL_TOKEN_PATH` to be a file called `*-token.json` in the same directory

    e.g:
    ```
    example.py 

    GMAIL_CREDENTIALS_PATH = "credentials.json"
    GMAIL_TOKEN_PATH = "token.json"
    ...
    ```

### Usage 

API Documentation is here: https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/

* Use this function to get the gmail service and access to all messages (taken from the `quickstart.py` code):

```
example.py
...
from google_api import gmail

# get all attachments from e-mails containing 'test'
search_query = "test"
service = gmail.get_gmail_service(GMAIL_CREDENTIALS_PATH, GMAIL_TOKEN_PATH)
results = gmail.query_for_csv_or_xl_attachments(service, search_query)

# 1st Attachment found:
item = results[0]
df = item['data']
print('email: ' + item['emailsubject'])
print('filename: ' + item['filename'])
print("data sample: ")
print(df.head())

```

