def email_code(z):
    import smtplib
    from email.message import EmailMessage
    msg=EmailMessage()
    msg['Subject']='fraud alert'
    msg['From']='team'
    msg['To']=z
    msg.set_content("Your account is being accessed by some one")
    with open("filename.jpg","rb") as f:
        file_data=f.read()
        file_type="image/jpg"
        file_name=f.name
        msg.add_attachment(file_data,maintype="application",subtype=file_type,filename=file_name)
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("bpvvproject2@gmail.com","Project1@bpvv")
    server.send_message(msg)
    server.quit()