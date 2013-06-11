#!/usr/bin/python3
# -*- coding: utf-8 *-*

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
