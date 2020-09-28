import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in text file for reading.
with open('../static_resources/some_text.txt') as text_file:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(text_file.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'Sample Subject'
msg['From'] = 'noreply@pythonexercise.com'
msg['To'] = 'kunalphadnis99@live.com'

# Send the message via our own SMTP server.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp_client:
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.login('email_address', 'password')
    smtp_client.send_message(msg)
    smtp_client.quit()
