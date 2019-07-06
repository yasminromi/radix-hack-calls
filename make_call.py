from twilio.rest import Client

account_sid = 'ACcd5071d8b3949b7dd9b0a65a3b6dd58f'
auth_token = 'c03e65954bb6c81e42aedc7601e5942e'
client = Client(account_sid, auth_token)

def lambda_handler(event, context):
    
    call = client.calls.create( url='http://demo.twilio.com/docs/voice.xml',
                                to='+5521965636086',
                                from_='+551149496211')
                        
    return {
            'statusCode': 200,
            'body': json.dumps(call.sid)
    }