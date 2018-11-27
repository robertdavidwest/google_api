from google_api import gmail

GMAIL_CREDENTIALS_PATH = '/Users/rwest/databreakthroughs-gmail-credentials.json'
GMAIL_TOKEN_PATH = '/Users/rwest/databreakthroughs-gmail-token.json'

search_query = "Encrave"
service = gmail.get_gmail_service(GMAIL_CREDENTIALS_PATH,
                                  GMAIL_TOKEN_PATH)
csv_dfs = gmail.query_for_csv_attachments(service, search_query)

