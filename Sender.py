import smtplib
from email.mime.text import MIMEText
import config
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

EMAIL=config.EMAIL
PASSWORD=config.PASSWORD
server.login(EMAIL,PASSWORD)

#Enter reciever email list
email = ["a@gmail.com", "b@gmail.com", "c@gmail.com" ] 

#Subject of mail 
subject_of_mail = "Write Subject here."

#Enter message body
M = """\
<html>
  <head></head>
  <body>
    <p>
    Good Evening User,<br> <br>

Check our application for Winner of previously bid product <br>
( Winner name and winning bid has been announced ) <br> <br>

Try to make your unique strategy and apply the bids on recently launched session products. <br><br>

Have a nice day. 😃<br><br>

~Regards <br>
Bid2Win.V2<br>
    </p>
  </body>
</html>
"""
message=MIMEText(M, 'html') #if message in html format
# message=MIMEText(M) #if message is in string format

message["Subject"]=subject_of_mail 

for i in email:
    server.sendmail(EMAIL, i,message.as_string())
    print("Mail is successfully sent to " + str(i))