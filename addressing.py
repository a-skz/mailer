import smtplib, ssl
from getpass import getpass
from email.message import EmailMessage

class Recipient(object):
    def __init__(self, email, name=None):
        self.email = email
        self.name = name

    def __str__(self):
        return ('Email: {0} - Name: {1}').format(self.email, self.name)

class Sender(Recipient):
    def __init__(self, email, name=None):
        super().__init__()

    def send_email(self, recipient_set, content, subject=None):
        port = 465  # For SSL
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Server is closed when ident block is finished
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

            print('Trying to login.')
            # Login to the server
            server.login(self.email, getpass())
            print('Login successful.\n')
            print('Sending emails.')

            print('From: ', self.email)

            for recipient in recipient_set:
                # Creating message object
                message = EmailMessage()
                message['Subject'] = subject
                message['From'] = self.email
                message['To'] = recipient.email
                print('To: ', recipient.email)
                
                # Customizing message content
                custom_content = content.replace(' <recipient_name>', ' ' + recipient.name)
                custom_content = custom_content.replace('<sender_name>', ' ' + self.name)
                message.set_content(custom_content)

                # Sending message
                server.send_message(message)
                print('Email sent.')

        print('Done.')