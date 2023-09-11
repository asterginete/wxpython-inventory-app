import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    """
    Sends an email notification.
    :param subject: Subject of the email.
    :param body: Body content of the email.
    :param to_email: Recipient email address.
    :param smtp_server: SMTP server address.
    :param smtp_port: SMTP server port.
    :param smtp_user: SMTP server user.
    :param smtp_pass: SMTP server password.
    :return: True if email sent successfully, False otherwise.
    """
    try:
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = smtp_user
        msg['To'] = to_email

        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)

        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
