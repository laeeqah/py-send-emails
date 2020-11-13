from tkinter import *
import smtplib

root = Tk()
root.geometry("500x500")
root.title("Send Email")
root.configure(background = "pink")
# creating SMTP




to_email = Label(root, text = "Email")
to_email.pack(pady = 15)

email_id = StringVar()
body_info =StringVar()
subj = StringVar()

email_entry = Entry(textvariable = email_id, width = 40)
email_entry.pack()

subject = Label(root, text = "Subject")
subject.pack(pady = 15)
sub_ent = Entry(textvariable = subj, width = 40)
sub_ent.pack()

message = Entry(textvariable = body_info, width = 40)
message.place(x = 100, y = 200, height = 50)


def gmail():
    usermail = email_id.get()
    body_content = body_info.get()
    print(usermail, body_content)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        sender_email = ("laeeqahesau@gmail.com")
        receiver_email = ("laeeqahesau@gmail.com")
        password = input("Enter senders email password")

        #starting TLS security
        server.starttls()

        server.login(sender_email, password)
        server.sendmail(sender_email,receiver_email, "This is a test email")
        print("This message has been sent successfully")
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
