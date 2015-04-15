#| ************* | ******************************* |
#| Author:       | Keith H.                        |
#| Date Created: | 04/15/2015                      |
#| Purpose:      | To Test the SendEmail.py script |
#|               |                                 |
#| ************* | ******************************* |
#!/usr/bin/env python

#import send_email method from SendEmail.py
from SendEmail import send_email

"""Defaults"""
EMAIL_SUBJECT = "Test Subject"
EMAIL_FROM = "From@domain.com"
EMAIL_RECIPIENTS = ['To@domain.com']

def test():
    EMAIL_SUBJECT = "TEST"
    send_email("TEST!", EMAIL_SUBJECT, EMAIL_FROM, EMAIL_RECIPIENTS)

#Main
def main():
    test()

#If the script is run by itself then call main
if __name__ == "__main__":
   main()
