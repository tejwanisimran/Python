######################################################################
# Program : Simple Gmail Mail Sender
# Author  : Simran Naveen Tejwani
# Purpose : Send mail using Python SMTP
######################################################################

import smtplib
from email.message import EmailMessage

######################################################################
# Function    : Marvellous_send_mail
# Description :  Send mails using Gmail SMTP server
######################################################################

def Marvellous_send_mail(sender , app_password,receiver,subject,body):
    # Step 1 : Create Email object
    msg = EmailMessage()

    # Step 2 : Set mail Headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    # Step 5 : Login using Gmail + App Password
    smtp.login(sender,app_password)

    # Step 6 : Send the mail
    smtp.send_message(msg)

    #Step 7 : Close the connection manually
    smtp.quit()

######################################################################
# Function    : main
# Description :  Driver code
######################################################################

def main():

    # Always use separate temporary/testing account
    sender_email = "marvellouspythondemo11@gmail.com"

    # App password generated from the google account
    app_password = "ghcb sqsi njkg qocf"

    # Your second mail for testing
    receiver_email = "tejwanisimran1802@gmail.com"

    subject = "Test Mail from the Python Script"

    body = """Jay Ganesh,
            This is a test mail sent using Marvellous Python.
            Regards.
            Marvellous Infosystems
            """
    
    Marvellous_send_mail(sender_email,app_password,receiver_email,subject,body)

    print("Marvellous Mail sent Successfully")

######################################################################
# Program Entry Point
######################################################################

if __name__ == "__main__":
    main()


