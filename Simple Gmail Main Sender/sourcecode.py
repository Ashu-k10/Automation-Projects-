#==========================================
# Program: Simple Gmail Main Sender                           #
# Author : Ashutosh Kadu                               
# Purpose : Send mail using Python SMTP                                 
#==========================================

import smtplib
from email.message import EmailMessage

#===========================================
# Function :   Marvellous_send_mail
# Description : Send email using Gmail SMTP Server
#===========================================

def send_mail(sender,app_password,receiver,subject,body):

    # Email object
    msg = EmailMessage() 

    # set main headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Add mail body
    msg.set_content(body)

    # Create SMTP SSL Connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # login using Gmail + App password
    smtp.login(sender,app_password)

    # Send the email
    smtp.send_message(msg)

    # Close connection manually
    smtp.quit()

#===========================================
# Function : main
# Description : Driver Code
#===========================================

def main():
    # Always use separate temporary/testing account
    sender_email = "ashutoshkadu6@gmail.com"

    # App password generated from google Account
    app_password = "xxxx xxxx xxxx xxxx"

    # Your second email for testing
    receiver_email = "ashutoshkadu6@gmail.com"

    subject = "Test Mail from python Script"

    body = """Jay Ganesh,


Regards,
Marvellous Infosystems
"""

    send_mail(
        sender_email,
        app_password,
        receiver_email,
        subject,
        body
    )

    print("Marvellous Mail sent Successfully")
    
#------------------------------------------------------
# Program Entry Point
# -----------------------------------------------------
if __name__ == "__main__":
    main()
