from pyfiglet import Figlet
import colorama
import click
import smtplib
import ssl
import email
import time
from PyInquirer import prompt
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL

header = Figlet(font="slant")
print(header.renderText("CLEMAIL"))

questions = [
    {
        'type': 'input',
        'name': 'sender_email',
        'message': 'Enter the from email',
    },
    {
        'type': 'input',
        'name': 'receiver_email',
        'message': 'Enter the receiver email',
    }
]


subject = "Send an attachment"
body = "Here is the attachment"
sender_email = "tracer00122132@gmail.com"
receiver_email = "tanmaych32@gmail.com"

# Create a multipart message and set headers
message = MIMEMultipart()
message["from"] = sender_email
message["to"] = receiver_email
message["subject"] = subject

# Attach body to email
message.attach(MIMEText(body, "plain"))

filename = "sarthak_chaudhari.pdf"

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()


@click.command()
def start():
    """Test script"""
    # Create a secure SSL context
    context = ssl.create_default_context()

    answers = prompt(questions)
    print(answers['sender_email'])

    # with click.progressbar([x for x in range(100)], color="red") as bar:
    #     for i in bar:
    #         time.sleep(0.1)

    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.login(sender_email, "tracer00!")
    #     server.sendmail(sender_email, receiver_email, text)

    click.clear()
    click.secho("Message Sent!", fg="bright_red")
