# Create a free account on twilio
# https://www.twilio.com/console

from twilio.rest import Client 
 
account_sid = '**************************************' 
auth_token = '****************************' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG6a24c8722f6f101db082a6edded36073', 
                              body='potato potatooo',      
                              to='******************' 
                          ) 
 
print(message.sid)