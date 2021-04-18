# EMAIL Module: https://docs.python.org/3/library/email.examples.html
# EMAIL Module legacy: https://docs.python.org/3/library/email.html#module-email
# SMTP: https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
import smtplib
from email.message import EmailMessage

# To send email, we need to set up a server. smtplib is used to set up a server
# for communication

# SMTP: Simple Mail Transfer Protocol

email = EmailMessage()
email['from'] = 'Gursewak Sidhu'
email['to'] = 'xxxxxxx@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'
email.set_content('Are you dumb enough to believe it')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #hello message, telling server is awake
    smtp.starttls() # encryption method
    smtp.login('emailid@gmail.com', 'password')
    smtp.send_message(email)
    print('All good boss')
    
