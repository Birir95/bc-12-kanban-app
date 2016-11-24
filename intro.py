import click
import sys
import time
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from tabulate import tabulate


def app_intro():
    click.secho('=' * 75, fg='white')
    click.secho('*' * 75, fg='yellow')
    click.secho('=' * 75, fg='white')
    init(strip=not sys.stdout.isatty())  # # strip colors if stdout is redirected
    cprint(figlet_format('KanBan App', font='big'), 'green')
    click.secho('*' * 75, fg='white')
    click.secho('=' * 75, fg='yellow')
    click.secho('*' * 75, fg='white')

def intro_msg():
    click.secho(
        """
    =================WELL HELLO THERE!===============
        """, bold=True, fg='blue')

def intro_header():
    click.clear()
    app_intro()

    with click.progressbar(range(50000), fill_char=click.style('#', fg='white', bg='red')) as prog_bar:
        for i in prog_bar:
            pass

    click.secho('' * 75)
    click.secho('' * 75)
    intro_msg()