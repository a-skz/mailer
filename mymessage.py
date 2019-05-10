from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Message(object):

    def __init__(self):
        self.__sender = ''
        self.__receiver = ''
        self.__subject = ''
        self.__body = ''
        self.__original_body = ''

    def set_sender(self, sender):
        self.__receiver = sender

    def set_receiver(self, receiver):
        self.__receiver = receiver

    def set_subject(self, subject):
        self.__subject = subject

    def set_body(self, path):
        txt_file = open(path, mode='r', encoding='utf-8')
        content = txt_file.read()
        txt_file.close()
        self.__body = content
        self.__original_body = content

    def custom_name(self, name):
        body = self.__original_body
        
        if name=='': 
            body = body.replace(' <name>', '')
        else:
            body = body.replace(' <name>', ' '+name)
        
        self.__body = body

    def get_message(self):
        message = MIMEMultipart()
        message["Subject"] = self.__subject
        message["From"] = self.__sender
        message["To"] = self.__receiver
        
        plain_text = MIMEText(self.__body, 'plain', _charset='utf-8')
        message.attach(plain_text)

        return message.as_string()