import smtplib
import os
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = "anandkallagunta@gmail.com"
EMAIL_PASSWORD = "8919293927"

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
msg =EmailMessage()
msg['Subject']="this is for indication?"
msg['From'] = EMAIL_ADDRESS
msg['To'] ='anandkallagunta@gmail.com'
msg.set_content('how you got email automatically')
with open("flag.jpg",'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(None, file_data)
    file_name = f.name

msg.add_attachment(file_data, maintype = 'image', subtype = file_type)

try:
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    # with smtplib.SMTP('localhost',1025) as smtp:
    # with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        # smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

        # subject = 'this is for indication?'
        # body = 'how you get email automatically'
        # msg = f'subject: {subject}\n\n{body}'

        # smtp.sendmail(EMAIL_ADDRESS,'anandkallagunta@gmail.com',msg)
        smtp.send_message(msg)
except  Exception as a:
    print('error while sending emial=',a)

finally:
    print('any execute this statement')
