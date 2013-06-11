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
# Developed by Nicolas Crocfer (http://www.shatter.fr)

try:
    import readline
except ImportError:
    import pyreadline.rl_windows as readline

from core.commands import CommandsManager


class CompleterManager:

    def __init__(self):
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.completer)
        self.commands = CommandsManager().commands()

    def completer(self, text, state):
        results = [x + " " for x in self.commands if x.startswith(text)] + [None]
        return results[state]
