from google_api import gmail

GMAIL_CREDENTIALS_PATH = '/Users/rwest/databreakthroughs-gmail-credentials.json'
GMAIL_TOKEN_PATH = '/Users/rwest/databreakthroughs-gmail-token.json'

search_query = "Encrave"
service = gmail.get_gmail_service(GMAIL_CREDENTIALS_PATH,
                                  GMAIL_TOKEN_PATH)
csvs_and_excel = gmail.query_for_csv_or_xl_attachments(service, search_query)

# 1st Attachment found:
item = csvs_and_excel[0]
df = item['data']
print('email: ' + item['emailsubject'])
print('filename: ' + item['filename'])
print("data sample: ")
print(df.head())
