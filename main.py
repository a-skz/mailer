from addressing import Sender, Recipient

recipient_set = [Recipient('email_1@email.com', 'name_1'),
                Recipient('email_2@email.com', 'name_2')]

sender = Sender('email_0@email.com', 'name_0')

with open('path_to_text', encoding='utf-8') as txt:
    content = txt.read()

subject = 'Subject'

sender.send_email(recipient_set, content, subject)