from pyfiglet import Figlet
import colorama
import click
import smtplib
import ssl
import email
import time
from PyInquirer import prompt, style_from_dict, Token
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465  # For SSL

header = Figlet(font="slant")

style = style_from_dict({
    Token.QuestionMark: '#fac731 bold',
    Token.Answer: '#4688f1 bold',
    Token.Instruction: '',  # default
    Token.Separator: '#cc5454',
    Token.Selected: '#0abf5b',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'input',
        'name': 'receiver_email',
        'message': 'Enter the receiver email:',
    },
    {
        'type': 'input',
        'name': 'sender_email',
        'message': 'Enter the sender email:',
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'Enter the password:',
    },
    {
        'type': 'input',
        'name': 'subject',
        'message': 'Enter the subject:',
    },
    {
        'type': 'input',
        'name': 'body',
        'message': 'Enter the body:',
    },
    {
        'type': 'confirm',
        'name': 'isAttachment',
        'message': 'Does your email contain an attachment:'
    }
]


# filename = ""

# # Open PDF file in binary mode
# with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())

# # Encode file in ASCII characters to send by email
# encoders.encode_base64(part)

# # Add header as key/value pair to attachment part
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )

# # Add attachment to message and convert message to string
# message.attach(part)

def create_attachment_email(message):
    """Function to create an email with attachment files"""
	message.attach(MIMEText(message["body"], "plain"))
	filename = input("Enter filename with extension :")
	path = input("Enter  the Path of the file :")
 	attachment = open(path, "rb")
	part = MIMEBase('application', 'octet-stream') 
 	part.set_payload((attachment).read()) 
 	encoders.encode_base64(part) 
  	part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
   	message.attach(part)
   	text = message.as_string()
   	return text



def create_text_email(message):
    """Function to create a text-based email"""
    # Attach body to email
    message.attach(MIMEText(message["body"], "plain"))
    text = message.as_string()

    return text


# tracer00122132@gmail.com


@click.command()
def start():
    """Entry point"""
    click.secho(header.renderText("CLEMAIL"), fg="bright_blue")

    # Create a secure SSL context
    context = ssl.create_default_context()

    answers = prompt(questions, style=style)
    # Create a multipart message and set headers
    message = MIMEMultipart()

    if(answers['isAttachment']) == True:
        password = answers["password"]
        message["from"] = answers['sender_email']
        message["to"] = answers['receiver_email']
        message["subject"] = answers['subject']
        message["body"] = answers["body"]
        text=create_attachment_email(message)
    else:
        # Extract the information from the prompt questions
        password = answers["password"]
        message["from"] = answers['sender_email']
        message["to"] = answers['receiver_email']
        message["subject"] = answers['subject']
        message["body"] = answers["body"]
        text = create_text_email(message)

    # Progressbar(Just for fun)
    with click.progressbar([x for x in range(100)], label=click.secho("Sending email...", fg="bright_red")) as bar:
        for i in bar:
            time.sleep(0.1)

    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.login(answers["sender_email"], answers["password"])
    #     server.sendmail(answers["sender_email"],
    #                     answers["receiver_email"], text)

    click.clear()
    click.secho("Email Sent!", fg="bright_red")
