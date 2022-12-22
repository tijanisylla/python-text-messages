from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()



def send_message(destination:str,message:str):
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message,
        from_ = twilio_number,
        to= destination
    )
    \

def main():
    target_number = input('Please enter a target number : ');
    message = input('Please type your message : ')
    # message_extention:str = us_extention + " " + message
    send_message(target_number, message)
    
    if(target_number):
        print(f" {message} is sent to ==> {target_number}")

if __name__ == '__main__':
    main()


