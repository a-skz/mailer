import getpass
import smtplib, ssl
import time

class Email(object):

    def __init__(self, sender):
        self.__sender = sender
        self.__receivers = []

    def set_receivers(self, receivers):
        self.__receivers = receivers

    def __get_password(self):
        password = getpass.getpass()
        return password

    def send_message(self, message) -> None:
        port = 465  # For SSL

        # Create a secure SSL context
        context = ssl.create_default_context()

        # server is closed when ident block is finished
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

            print('Trying to login.')
            server.login(self.__sender, self.__get_password())
            print('Login successful.\n')
            print('Sending emails.')

            message.set_sender(self.__sender)
            print('From: ', self.__sender)

            for receiver in self.__receivers:

                message.set_receiver(receiver)
                print('To: ', receiver)
                
                server.sendmail(self.__sender, receiver, message.get_message())
                print('Email sent.')
                
                time.sleep(5)
        
        print('Done.')