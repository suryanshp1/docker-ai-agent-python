from email.message import EmailMessage
import smtplib
import os

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = os.getenv("EMAIL_PORT", 465)

def send_mail(subject: str = "No subject provided", content: str = "No message provided", to_email: str = EMAIL_ADDRESS, from_email: str = EMAIL_ADDRESS):
    try:
        msg = EmailMessage()
        msg.set_content(content)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email
        msg.set_content(content)

        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            return server.send_message(msg)
    except smtplib.SMTPAuthenticationError as e:
        print("\n❌ Authentication Failed!")
        print("This is likely because you are using your regular Gmail password.")
        print("Google requires an 'App Password' for third-party apps.")
        print("1. Go to https://myaccount.google.com/security")
        print("2. Enable 2-Step Verification")
        print("3. Search for 'App Passwords' and create one")
        print("4. Update EMAIL_PASSWORD in your .env file with the 16-character App Password\n")
        raise e
    except Exception as e:
        raise e
