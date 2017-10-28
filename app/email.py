import yagmail
from app.settings import Config

class Email:
    def __init__(self):
        self.YAG = yagmail.SMTP(Config.EMAIL_USERNAME)

    def send_new_magazine_mail(self, magazines, date):
        subject = 'New magazines available!'
        magazines_str = self.magazines_to_str(magazines)
        body = f"\
        Date: {date}\n\n\
        {magazines_str}\
        "

        self.YAG.send(to=Config.EMAIL_TO, subject=subject, contents=body)

    def magazines_to_str(self, magazines):
        res = ""
        for title, url in magazines:
            res += f'{title}\n{url}\n\n'

        return res