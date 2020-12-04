from twilio.rest import Client

account_sid = "AC5babcfbb2903db3a91d4d7e0c002dc9"
auth_token = "74ac5753df0e26e0f6c9fb5a101f357"
my_cell = "+918660145513"
my_twilio = "12513295012"


client = Client(account_sid, auth_token)

my_message = "Hi Buddy..."

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_message)
