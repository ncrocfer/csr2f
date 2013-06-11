#!/usr/bin/python3
# -*- coding: utf-8 *-*

import signal

from core.completer import CompleterManager
from core.commands import *


class Manager:

    def __init__(self):
        self.completer = CompleterManager()
        pass

    def sigint_handler(self, s, f):
        om.info("Bye", begin="\n")
        exit(0)

    def run(self):
        signal.signal(signal.SIGINT, self.sigint_handler)
        om.info("{} exploits loaded\n".format(em.get_number()))

        while True:
            line = input("csr2f> ")

            try:
                cmd_name = line.strip().split()

                if len(cmd_name) > 0 and len(cmd_name[0]) > 0:
                    cmd = CommandsManager().find(cmd_name[0])
                    cmd.run(cmd_name[1:] if len(cmd_name) > 1 else [])
            except CmdNotExistsException as e:
                om.error('Error : {}'.format(e))
