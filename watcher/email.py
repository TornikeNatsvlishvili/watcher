import yagmail
from watcher.settings import Config

class Email:
    def __init__(self):
        user = Config.secrets['email']['username']
        password = Config.secrets['email']['pass']
        self.YAG = yagmail.SMTP(user, password)

    def send_new_magazine_mail(self, magazines, date):
        subject = 'New magazines available!'
        magazines_str = self.magazines_to_str(magazines)
        body = f"\
        Date: {date}\n\n\
        {magazines_str}\
        "

        self.YAG.send(to=Config.secrets['email_to'], subject=subject, contents=body)

    def magazines_to_str(self, magazines):
        res = ""
        for title, url in magazines:
            res += f'{title}\n{url}\n\n'

        return res