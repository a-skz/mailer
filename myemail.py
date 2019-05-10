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

    def send_messages(self, message, names=[]):
        port = 465  # For SSL
        sender = self.__sender
        receivers = self.__receivers
        # Create a secure SSL context
        context = ssl.create_default_context()

        # server is closed when ident block is finished
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

            print('Trying to login.')
            server.login(sender, self.__get_password())
            print('Login successful.\n')
            print('Sending emails.')

            message.set_sender(sender)
            print('From: ', sender)
            
            while (len(names)!=len(receivers)): names.append('')

            for receiver, name in zip(receivers,names):

                message.set_receiver(receiver)
                print('To: ', receiver)
                message.custom_name(name)                                
                    
                server.sendmail(self.__sender, receiver, message.get_message())
                time.sleep(1)
                print('Email sent.')
                
        print('Done.')