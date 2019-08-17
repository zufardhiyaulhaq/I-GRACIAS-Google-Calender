from __future__ import print_function
import httplib2

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime
import json
import os

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
# Program Create by Zufar Dhiyaulhaq


SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_id.json'
APPLICATION_NAME = 'I-GRACIAS GOOGLE CALENDER'
DATABASE_TMP = json.load(open("data.json","r"))
DATABASE = DATABASE_TMP["JSON"]

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
        credentials = tools.run_flow(flow, store, flags)
    return credentials

def main(year,month,day,until_date):

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    length = len(DATABASE['aaData'])
    start = 0

    while start<length:
        if DATABASE['aaData'][start][0] == 'SENIN':
            date = year+'-'+month+'-'+str(day)
        elif DATABASE['aaData'][start][0] == 'SELASA':
            date = year+'-'+month+'-'+str(day+1)
        elif DATABASE['aaData'][start][0] == 'RABU':
            date = year+'-'+month+'-'+str(day+2)
        elif DATABASE['aaData'][start][0] == 'KAMIS':
            date = year+'-'+month+'-'+str(day+3)
        elif DATABASE['aaData'][start][0] == 'JUMAT':
            date = year+'-'+month+'-'+str(day+4)
        elif DATABASE['aaData'][start][0] == 'SABTU':
            date = year+'-'+month+'-'+str(day+5)

        event = {
            'summary': DATABASE['aaData'][start][4],
            'location': DATABASE['aaData'][start][2],
            'description': 'Telkom University',
            'start': {
                'dateTime': date+'T'+DATABASE['aaData'][start][1]+'+07:00',
                'timeZone': 'Asia/Jakarta'
            },
            'end': {
                'dateTime': date+'T'+DATABASE['aaData'][start][7]+'+07:00'
,
                'timeZone': 'Asia/Jakarta'
            },
            'recurrence': [
                'RRULE:FREQ=WEEKLY;UNTIL='+until_date+'T000000Z',
            ],
            'reminders': {
                'useDefault': True
            }
        }

        print(json.dumps(event))
        eventr = service.events().insert(calendarId='primary', body=event).execute()

        start+=1

print (" I-GRACIAS GOOGLE CALENDER")
date = str(input(" input hari pertama (yyyymmdd) : "))
until = str(input(" input tanggal terakhir jadwal berakhir (yyyymmdd) : "))

year = date[0:4]
month = date[4:6]
day = int(date[6::])

main(year,month,day,until)

