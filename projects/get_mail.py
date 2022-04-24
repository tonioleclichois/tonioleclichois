import datetime
import imaplib
import email
from email.header import decode_header
import pandas as pd


imap = imaplib.IMAP4_SSL('outlook.office365.com')
m = imap.login('antoinedemuizon@hotmail.fr', 'Jesus1inmylife')

imap.select(mailbox="LYDIA")

(status, searchRes) = imap.search(None, 'ALL')  # Récupération des numéros des messages
ids = searchRes[0].split()
# print(ids[-10943])
counter = 0
# for i in range(len(ids)-70, len(ids)):
for i in range(len(ids)):
    (status, res) = imap.fetch(ids[i], '(RFC822)')
    for responsePart in res:
        if isinstance(responsePart, tuple):
            r = responsePart[1].decode("utf-8")
            msg = email.message_from_string(r)
            date_mail = msg['Date']
            sender = msg['from']
            # print(msg(['date']))
            print("date_mail", date_mail)
            # print("sender", sender)
            # print("\n\n responsePart \n\n", responsePart[1])
            # print(datetime.datetime.strptime(date_mail, '%d/%m/%y %H:%M:%S'))
            if "lydia" in sender:
                subject = msg['subject']
                print('\n HERE')
                print('expediter : ', sender[sender.find('<')+1:sender.find('>')])
                print(subject)
                objet = decode_header(subject)[0][0].decode("utf-8")
                print(objet.split())
                numbers = [int(temp[0:temp.find(',')]) for temp in objet.split() if temp[0].isdigit()]
                if objet.split()[0] == '+' or objet.split()[0] == '-':
                    print('subject décodé : ', numbers)
                    counter += numbers[0]
                    print(counter)

                # dldate = email.utils.parsedate(date_mail)
                # pd_dt = pd.DataFrame({'year': [dldate[0]],
                #                       'month': [dldate[1]],
                #                       'day': [dldate[2]]
                #                       })
                # print(pd_dt)
                # print("parse", dldate)
                # print("mktime", datetime.datetime.fromtimestamp(pd.to_datetime(pd_dt)))


# email.utils.parsedate('Mon, 16 Nov 2009 13:32:02 +0100')
# (2009, 11, 16, 13, 32, 2, 0, 1, -1)
# >>> time.mktime((2009, 11, 16, 13, 32, 2, 0, 1, -1))
# 1258378322.0
# >>> datetime.datetime.fromtimestamp(1258378322.0)
# datetime.datetime(2009, 11, 16, 13, 32, 2)

imap.close()
imap.logout()
