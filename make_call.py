import json
import requests
from twilio.rest import Client


account_sid = 'ACf737a865f5030947224ce86063f4806b'
auth_token = 'bebc51d8e5fc8678825df24190968d82'

api_url_base = 'http://localhost:8000/sendMessage'

client = Client(account_sid, auth_token)

call = client.calls.create( url='https://raw.githubusercontent.com/yasminromi/radix-hack-calls/master/call.xml',
                            to='+5521986858723',
                            from_='+551149507127')

data = '''{
    "_id": "97",
    "category": "call",
    "call" : ["aumentar", "20", "kv"],
    "user" : {
        "name": "+551149507127",
		"msisdn": "551149507127"
    }
}'''

response = requests.post(api_url_base, data=data,headers={"Content-Type": "application/json"})

print(call.sid)
print(response)