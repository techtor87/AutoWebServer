from consts import *
from time import localtime, strftime
from exchangelib import DELEGATE, Account, Credentials, \
        EWSDateTime, EWSTimeZone, Configuration, NTLM, Message, \
        Mailbox, Attendee, Q
from exchangelib.folders import ExtendedProperty, FileAttachment, ItemAttachment, \
        HTMLBody
import locale

def send_email():
    #locale.setlocale(locale.LC_ALL,'')
    credentials = Credentials(username='LOGON\\210060583', password='adel2016phikos')
    account = Account(  primary_smtp_address='gregory.faulconbridge@ge.com',
                        credentials=credentials,
                        autodiscover=True,
                        #locale=locale.getlocale()
                        )
    m = Message(
            account = account,
            folder = account.sent,
            subject = 'testing 123',
            body = 'tesing 321',
            to_recipients=[Mailbox(email_address='gfaulconbridge@gmail.com')]
            )
    m.send_and_save()

    print("send email")
    pass

if __name__ == '__main__':
    send_email()
