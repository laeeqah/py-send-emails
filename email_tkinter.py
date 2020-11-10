from tkinter import *
import smtplib

root = Tk()
root.geometry("500x500")
root.title("Send Email")
# creating SMTP

to_email = Label(root, text = "Email")
to_email.pack(pady = 15)
email_entry = Entry(root)
email_entry.pack()

subject = Label(root, text = "Subject")
subject.pack(pady = 15)
sub_ent = Entry(root)
sub_ent.pack()

message = Text(root, width = 40, height = 10)
message.pack(pady = 10)

def gmail():
    usermail = email_entry.get()
    server = smtplib.SMTP("smtp.gmail.com', 587")
    subj = sub_ent.get()
    text = message.get()
    password = password.get()
    server.starttls()
    main_message = message.get()

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



send_btn = Button(root, text ="Submit", command = gmail)
send_btn.pack()

def clear_all():
    email_entry.delete(0, "end")
    sub_ent.delete(0,"end")
    message.delete("1.0","end")

clear_btn = Button(root, text = "Clear", command = clear_all)
clear_btn.pack()


root.mainloop()
