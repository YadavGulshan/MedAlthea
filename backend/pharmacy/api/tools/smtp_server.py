from os import environ
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class smtp_server:
    def send_email(send_to:str, url:str):
        print("Sending email to: " + send_to)
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        send_from = environ.get("EMAIL")
        password = environ.get("PASSWORD")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Account Verification"
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
                """.format(url)

        part = MIMEText(text, "html")
        message.attach(part)

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls(context=context)
                server.login(send_from, password)
                server.sendmail(send_from, send_to, message.as_string())
                server.close()
                print("Email sent!")
        except Exception as e:
            print("Error:", e)
            return False
        return True


if __name__ == "__main__":
    smtp_server.send_email("yadavgulshan542@gmail.com", "gulshan.cf")