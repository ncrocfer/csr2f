#!/usr/bin/python3
# -*- coding: utf-8 *-*

import sys


class OutputManager:

    def __init__(self):
        self.new_line = "\n"

    def info(self, string, begin='', end='\n'):
        string = begin + "[+] " + string + end
        sys.stdout.write(string)
        sys.stdout.flush()
        return self

    def error(self, string, begin='', end='\n'):
        string = begin + "[-] " + string + end
        sys.stdout.write(string)
        sys.stdout.flush()
        return self
