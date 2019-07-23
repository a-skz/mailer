import csv
from addressing import Sender, Recipient

with open('recipient_list.csv', encoding='utf-8', newline='') as csvfile:
    recipient_list = csv.reader(csvfile, delimiter=',')
    next(recipient_list)
    recipient_set = [Recipient(recipient[0], recipient[1]) for recipient in recipient_list]

sender = Sender('email_0@email.com', 'name_0')

with open('path_to_text', encoding='utf-8') as txt:
    message_content = txt.read()
message_subject = 'Subject'

sender.send_email(recipient_set, message_content, message_subject)