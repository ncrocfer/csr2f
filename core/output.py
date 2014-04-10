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
