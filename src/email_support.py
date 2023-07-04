```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_support(student_data, tutor_data, subject, message):
    # Set up the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to the email account
    server.login("your-email@gmail.com", "your-password")

    # Create a message
    msg = MIMEMultipart()

    # Set the message parameters
    msg['From'] = "your-email@gmail.com"
    msg['To'] = student_data['email']
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    # Send the message
    server.send_message(msg)

    # Close the server connection
    server.quit()
```