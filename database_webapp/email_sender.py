import smtplib
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self, email, height, average_height, count):
        self.email = email
        self.height = height
        self.average_height = average_height
        self.count = count

    def send_email(self):
        from_email = ""
        from_password = ""
        to_email = self.email
        subject = "Height data"
        message = (
            "Your height is <strong>%s</strong>. Average height of all is %s from %s users"
            % (self.height, self.average_height, self.count)
        )
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email

        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(from_email, from_password)
        gmail.send_message(msg)
