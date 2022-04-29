from os import environ
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading


class smtp_server(threading.Thread):
    def __init__(self, email, subject, message):
        threading.Thread.__init__(self)
        self.email = email
        self.subject = subject
        self.message = message

    def run(self):
        print("Sending email to: " + self.email)
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        send_from = environ.get("EMAIL")
        password = environ.get("PASSWORD")

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = send_from
        text = """\
                <html>
                  <body>
                    <p>Hi,<br>
                       This message is sent from the MedAlthea.<br>Please click the link below to verify your account.<br>
                        {}
                    </p>
                  </body>
                </html>
                """.format(
            self.message
        )

        part = MIMEText(text, "html")
        message.attach(part)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(send_from, password)
                server.sendmail(send_from, self.email, message.as_string())
                server.close()
                print("Email sent!")
        except Exception as e:
            print("Error:", e)
            return False
        return True


if __name__ == "__main__":
    smtp_server.send_email("yadavgulshan542@gmail.com", "gulshan.cf")
