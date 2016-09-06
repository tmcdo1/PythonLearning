# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC343e7adfbbd49b0597fb052e491e9c76"
auth_token = "dce59c266e372eb1adf5da88ae459038"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+12817700290", from_="+12036016507",
                                     body="Hola padre. My python program is sending you this :)")
