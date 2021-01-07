import smtplib

from string import Template
from email.encoders import encode_base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase





def email(address,sub, message, filepath):
    import ntpath
    filename = ntpath.basename(filepath)
    MY_ADDRESS = 'projectpiscestx@gmail.com'
    PASSWORD = 'senioritis123'

    # set up the SMTP serversmtplib.SMTP('smtp.gmail.com', 587)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template


    # Prints out the message body for our sake
    print(message)

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath, "rb").read())
    encode_base64(part)

    part.add_header('Content-Disposition', f'attachment; filename="{filename}"')

    msg.attach(part)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    # msg['To']='kvaldez2000@gmail.com'
    msg['To']= address
    msg['Subject']=sub
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
    
    # Terminate the SMTP session and close the connection
    s.quit()
    
