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
import os
import getopt
import builtins

from core.config import ConfigManager
from core.output import OutputManager
from core.exploits import ExploitsManager
from core.manager import Manager

__version__ = "0.2"
__author__ = "Nicolas Crocfer"
__licence__ = "GPLv3"


def banner():
    print(
'''
*********************************************************
*                                                       *
*     ______   ______   _______      _____   ________   *
*   .' ___  |.' ____ \ |_   __ \    / ___ `.|_   __  |  *
*  / .'   \_|| (___ \_|  | |__) |  |_/___) |  | |_ \_|  *
*  | |        _.____`.   |  __ /    .'____.'  |  _|     *
*  \ `.___.'\| \____) | _| |  \ \_ / /_____  _| |_      *
*   `.____ .' \______.'|____| |___||_______||_____|     *
*                                                       *
*         Cross Site Request Forgery Framework          *
*                                                       *
* Version  : {}                                        *
* Author   : {}                            *
* Website  : https://github.com/ncrocfer/csr2f          *
* Licence  : {}                                      *
*                                                       *
*********************************************************
'''.format(__version__, __author__, __licence__))


def usage():
    print(' Usage : ' + sys.argv[0] + ' [params]')
    print(' Run CSR2F to begin an interactive session\n')
    print(' Params can be:')
    print('   -h (help): Prints this help.')
    print('   -v (version): Prints the current version of CSR2F.')
    exit(0)


def version():
    om.info('CSR2F version {}\n'.format(str(__version__)))
    exit(0)


def parse_options():
    if '-h' in sys.argv:
        usage()
    elif '-v' in sys.argv:
        version()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:v")
    except getopt.GetoptError as e:
        om.error("Invalid parameter({})\n".format(str(e)))
        exit(1)
    return args


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    builtins.config = ConfigManager()
    builtins.om = OutputManager()
    builtins.em = ExploitsManager()

    banner()
    options = parse_options()

    manager = Manager()
    manager.run()

    exit(0)
