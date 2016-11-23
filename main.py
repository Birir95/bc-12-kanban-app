#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    my_KanBan todo <task_name> <task_desc>
    my_KanBan doing <task_id> <task_start>
    my_KanBan list_to_do
    my_KanBan list_doing
    my_KanBan list_done
    my_KanBan list_all

    my_KanBan (-i | --interactive)
    my_KanBan (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from KanBan import ToDo


cd = ToDo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to KanBan program!' \
        + ' (type help for a list of commands.)'
    prompt = '(my_KanBan) '
    file = None

    @docopt_cmd
    def do_todo(self, arg):
        """Usage: todo <task_name> """
        task_desc=raw_input("Enter description :")

        cd.to_do(arg['<task_name>'],task_desc)

    @docopt_cmd
    def do_doing(self, arg):
        """Usage: doing <task_id> <task_start>"""
        try:
            task_id = int(arg['<task_id>'])
            cd.doing(task_id, arg['<task_start>'])
        except(ValueError):
            print "Id should be an integer"

    @docopt_cmd
    def do_done(self, arg):
        """Usage: done <task_id> <task_stop>"""

        cd.done(arg['<task_id>'], arg['<task_stop>'])

    @docopt_cmd
    def do_list_to_do(self, arg):
        """Usage: list_to_do """

        cd.list_to_do()

    @docopt_cmd
    def do_list_doing(self, arg):
        """Usage: list_doing """

        cd.list_doing()

    @docopt_cmd
    def do_list_done(self, arg):
        """Usage: list_done """

        cd.list_done()

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_all """

        cd.list_all()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

#opt = docopt(__doc__, sys.argv[1:])

MyInteractive().cmdloop()

#print(opt)
