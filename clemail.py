from pyfiglet import Figlet
import click
import smtplib
import ssl

sender_email = "tracer00122132@gmail.com"
receiver_email = "sahilambre06@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

port = 465  # For SSL

header = Figlet(font="slant")
print(header.renderText("CLEMAIL"))


@click.command()
def start():
    """Test script"""
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("tracer00122132@gmail.com", "tracer00!")
        server.sendmail(sender_email, receiver_email, message)

    click.echo("Message sent!")
