import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject_heading, subject_link, receiver):

    msg = MIMEMultipart()
    msg2 = MIMEText("<h1>Hi,</h1>",'html')

    heading = MIMEText("<h3>" + subject_heading + "</h3>",'html')
    link    = MIMEText(subject_link)

    msg['Subject'] = "IPU NEW NOTICE"
    msg['From'] = "deepakvats97@gmail.com"

    recv = []
    recv.append(receiver)
    msg['To'] = ", ".join(recv)
    #msg.attach(msg2)
    msg.attach(heading)
    msg.attach(link)


    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('deepakvats97@gmail.com', '@btechece1#')

    smtpserver.sendmail('deepakvats97@gmail.com', recv, msg.as_string())
    smtpserver.quit()
