import argparse
import requests
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description='Codeforces User Information')
parser.add_argument('-H', '--handle', type=str, metavar='', help='Codeforces handle of the user')
parser.add_argument('-c', '--contests', type=bool, metavar='', nargs='?', const=True, help='View list of upcoming contests')
args = parser.parse_args()

if args.handle != None:
    response = requests.get('http://codeforces.com/api/user.info?handles=' + args.handle)
    if response.status_code != 200:
        print('Handle not found.')
    else:
        result = response.json()['result'][0]
        try:
            print('Full Name: ' + result['firstName'] + ' ' + result['lastName'])
        except:
            print('Name not available')
        print('Current Rating: ' + str(result['rating']))
        print('Rank: ' + str(result['rank']))
        try:
            print('Location: ' + result['city'] + ', ' + result['country'])
            print('Profile picture link: ' + result['titlePhoto'])
        except:
            pass

if args.contests != None and args.contests == True:
    response = requests.get('http://codeforces.com/api/contest.list')
    if response.status_code != 200:
        print('Error occured. Please try again later.')
    else:
        result = response.json()['result']
        print('\nUpcoming contests:\n')
        for contests in result:
            if contests['phase'] == 'BEFORE':
                sec = contests['relativeTimeSeconds']*-1
                sec = timedelta(seconds=int(sec))
                d = datetime(1, 1, 1) + sec
                print('ID: ' + str(contests['id']))
                print('Name: ' + contests['name'])
                print('Type: ' + contests['type'])
                print('Time left: ' + str(d.day-1) + ' days, ' + str(d.hour) + ' hours, ' + str(d.minute) + ' minutes, ' + str(d.second) + ' seconds.\n')
