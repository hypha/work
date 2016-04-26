import sys
from oauth2client.service_account import ServiceAccountCredentials
import gspread


def authorise():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(sys.argv[1], scope)
    return gspread.authorize(credentials)
