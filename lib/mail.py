"""
Mail
"""
from lib.settings import *
from lib.helpers import helpers
from smtplib import SMTP

class mail:
    @staticmethod
    def send(subject, message):
        try:
            server = SMTP(EMAIL_SERVER_URL, EMAIL_SERVER_PORT)

            server.ehlo() # Handshake
            server.starttls() # TLS needed for Gmail

            # Login with user and password
            server.login(EMAIL_SERVER_USERNAME, EMAIL_SERVER_PASSWORD)

            headers = "\r\n".join([
                "From: %s" % EMAIL_SERVER_USERNAME,
                "To: %s" % ", ".join(EMAILS),
                "Subject: %s" % subject,
                "MIME-Version: 1.0",
                "Content-Type: text/html"
            ])

            # Send mail to all addresses from env setting
            server.sendmail(EMAIL_SERVER_USERNAME, EMAILS, headers + "\r\n\r\n" + message)

            helpers.message("Sent email(s) to: " + ", ".join(EMAILS))

        except Exception as e:
            helpers.error(e)

        finally:
            server.quit()
