from pyfiglet import Figlet
import click

header = Figlet(font="slant")
print(header.renderText("CLEMAIL"))


@click.command()
def cli():
    """Test script"""
    click.echo("Hello World")
