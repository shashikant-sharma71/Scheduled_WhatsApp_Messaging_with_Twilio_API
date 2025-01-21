# Step 1  Install Required Libraries 

from twilio.rest import Client
from datetime import datetime, timedelta
import time 



# Setp 2  Twilio Credentials

account_sid='AC44a300feb2a3086d3666fd8f8b52450c' # It use to Twilio API Authenticate 
auth_token='619f8a94e627e5d82252aa58e2757d81'  # It use to Twilio API Authenticate
client = Client(account_sid,auth_token)  #   "Client Object " Used For Send Massage 








# Step 3  Define Send Masssage Function

def send_Whatsapp_Massage(recipient_number,message_body):  # Function to Send Whatsapp Massage 
    try:
        message=client.messages.create(   # "Client.messages.create" is a Twilio's method that send messages 
            from_= 'whatsapp:+14155238886',   # Twilio's Whatsapp Send-Box Number 
            body=message_body,  # Body is beasicaly messages  that we want to send
            to=f'whatsapp:{recipient_number}' # Where to send the Messages  "What is The Recipient Number"
        )
        print(f"Message Sent  Successfully!  Message SID {message.sid}")
        
    except Exception as e: # If there is an issue occured like Network problem or other issues then it will comes to exception block 
        print("An Error Occured")
        
    



# Step 4  User Input 

name = input("Enter The Reciepent Name")
recipient_number= input("Enter the Recipent Whatsapp Number with Country Code (e.g, +12345)")
message_body=input(f"Enter the message that you want to send to {name}: ")

#Step 5  Parse  date/time and Calculate delay 

date_str= input("Enter the date to send the message(YYYY-MM-DD):")
time_str= input("Enter the Time to send the message(HH:MM  in 24-hour formate ):")

# datetime

schedule_datetime= datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")

current_datetime=datetime.now()  #It's Fact the current Date time

# Calculate Delay 

time_difference=schedule_datetime-current_datetime  # It Calculate The Difference Between User time and Current time and Date also 

delay_seconds=time_difference.total_seconds() # It Will convert  the time into Seconds 

if delay_seconds<=0:
    print("The specify time is in the past. please enter a future date and time")
else:
    print(f"The message Scheduled to send to {name}at{schedule_datetime}.")
    
    # Wait Untill the Scheduled Time 
    time.sleep(delay_seconds) #1000   
    
    #Send the Massage 
    send_Whatsapp_Massage(recipient_number,message_body)