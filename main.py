from myemail import Email
from mymessage import Message

subject = 'Teste.'
path = 'message.txt'

sender = 'feflog.extensao@gmail.com'
receivers = ['aclsobrinho@hotmail.com', 'aclsobrinho@gmail.com']

message = Message()
message.set_subject(subject)
message.set_body(path)

email = Email(sender)
email.set_receivers(receivers)
email.send_message(message)