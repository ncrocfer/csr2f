#!/usr/bin/python3
# -*- coding: utf-8 *-*

import sys
import os
import getopt
import builtins

from core.config import ConfigManager
from core.output import OutputManager
from core.exploits import ExploitsManager
from core.manager import Manager

__version__ = "0.1b"
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
* Version  : {}                                       *
* Author   : {}                            *
* Website  : http://csr2f.github.com                    *
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
