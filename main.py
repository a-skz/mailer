from myemail import Email
from mymessage import Message

raw = """Email	Name"""

raw = raw.replace('\n','\t').split('\t')

names = [raw[i] for i in range(1,len(raw),2)]
receivers = [raw[i] for i in range(0,len(raw),2)]

subject = 'Test'
path = 'message.txt'

sender = 'myemail@gmail.com'

message = Message()
message.set_subject(subject)
message.set_body(path)

email = Email(sender)
email.set_receivers(receivers)
email.send_messages(message, names)

