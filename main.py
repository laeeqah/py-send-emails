# Sending Email Exercise via tkinter

from tkinter import *
import smtplib
# creating SMTP
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email = ("senders-email-address.com")
    receiver_email = ("thapelo@lifechoices.co.za")
    password = input("Enter senders email password")

    #starting TLS security
    server.starttls()

    server.login(sender_email, password)

    message = "Greeings"
    message2 = "Hi there .Get well soon\n"
    message = message + ""

    server.sendmail(sender_email, receiver_email, message, message2)

except Exception as error:
    print("Something went wrong...", error)
finally:
    server.quit()
