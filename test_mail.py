import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#sender="mickey.sun3@gmail.com"
#receiver=["mickey_sun0313@yahoo.com.tw","mickey_sun0313@yahoo.com.tw"]
passwd=""

for R in receiver :
    print(R)

    msg= MIMEMultipart()
    msg["From"]= sender
    msg["To"]= R
    msg["Subject"]= Header("Test send email","utf-8").encode()

    body="This is send by python\nhow are you?"

    msg_text=MIMEText(body)
    msg.attach(msg_text)
    c = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
      server.login(sender,passwd)
      server.sendmail(sender,R,msg.as_string())
    print("success send email!")
