from email.mime.text import MIMEText
import smtplib
    
def send_email(email, height, avg, count):
    from_email = "testitmail95@gmail.com"
    from_password = "oznznlgvoqmyszqe"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong> %s </strong> and average height of our users is <strong> %s </strong> based on <strong> %s </strong> users" % (height, avg, count)

    msg = MIMEText(message, 'html')
    msg['Subject']=subject
    msg["To"]=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

