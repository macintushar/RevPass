import PassCreater
from twilio.rest import Client

safepass = PassCreater.passw
safepass = str(safepass)
safePass = "New Password for the Safe:" + safepass

account_sid = 'AC5a99232f3129d32a4b49312f4566505d'
auth_token = '24cbfe5d21a3d02e7d8271497362a481'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=safePass,
                     from_='+12056228658',
                     to='+919110894405'
                 )

print(message.sid)
print("Current Safe password: ",safepass," has been sent to your phone by SMS.")