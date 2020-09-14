import PassCreater
from twilio.rest import Client

safepass = PassCreater.passw
safepass = str(safepass)
safePass = "New Password for the Safe:" + safepass

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=safePass,
                     from_='twilio_phone_number',
                     to='verified_phone_number'
                 )

print(message.sid)
print("Current Safe password: ",safepass," has been sent to your phone by SMS.")
