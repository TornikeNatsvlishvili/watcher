import yagmail
from app.settings import EMAIL_TO, EMAIL_USERNAME

USERNAME = 'tornikenatsvlishvilideveloper'
yag = yagmail.SMTP(USERNAME)

def send_new_magazine_mail(magazines, date):
    to = 'tornikenatsvlishvili@gmail.com'
    subject = 'New magazines available!'
    magazines_str = magazines_to_str(magazines)
    body = f"\
    Date: {date}\n\n\
    {magazines_str}\
    "

    yag.send(to=to, subject=subject, contents=body)

def magazines_to_str(magazines):
    res = ""
    for title, url in magazines:
        res += f'{title}\n{url}\n\n'

    return res