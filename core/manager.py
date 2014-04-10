#!/usr/bin/python3
# -*- coding: utf-8 *-*
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
#
# Developed by Nicolas Crocfer (https://github.com/ncrocfer)

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
        om.info("{} exploits loaded".format(em.get_number()))
        om.info("Last update : {}\n".format(em.get_last_update()))

        while True:
            line = input("csr2f> ")

            try:
                cmd_name = line.strip().split()

                if len(cmd_name) > 0 and len(cmd_name[0]) > 0:
                    cmd = CommandsManager().find(cmd_name[0])
                    cmd.run(cmd_name[1:] if len(cmd_name) > 1 else [])
            except CmdNotExistsException as e:
                om.error('Error : {}'.format(e))
