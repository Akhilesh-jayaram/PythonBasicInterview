#Working code from the below local gmail and mail server 
import smtplib
import email.mime.text
import email.mime.multipart

sender_email = "rajkumarsunil140@gmail.com"
receiver_email = "akhil31099@gmail.com"
password = "mipaqriuiynnmrrd"

msg = email.mime.multipart.MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Test Email"

text = email.mime.text.MIMEText("This is a test email sent using python")
msg.attach(text)

try:
 server = smtplib.SMTP("smtp.gmail.com", 587)
 server.ehlo()
 server.starttls()
 server.login(sender_email, password)
 server.send_message(msg)
      print ('Email sent!')
except Exception as e:
      print ('Something went wrong...', e)
finally:
     server.quit()
