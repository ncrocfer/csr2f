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

import os
from collections import OrderedDict

from core.exceptions import CmdNotExistsException
from core.exceptions import ParamsNotExistsException
from core.exceptions import UpdateException
from core.exploits import ExploitsManager
from core.generator import Generator


class HelpCommand():

    def run(self, params):

        if not params:
            print('''
\tCommands\tDescription
\t========\t===========\n
\tconfig  \tDisplay the configuration options
\tclear   \tClear the current screen
\tsearch  \tSearch an exploit based on keyword
\tshow    \tDisplay informations about an exploit based on its ID
\tset     \tSet special fields for an exploit
\tgenerate\tGenerate the exploit to the console or in a file
\tupdate  \tUpdate the exploits list
\thelp    \tPrint this help menu
\texit    \tExit the console

\thelp <command> to get the command's usage
''')
        elif params[0] == 'config':
            print('''\n\tThis command is used to view and modify the basic configuration. You
\tcan view it by typing 'config' without argument.

\tUsage:\tconfig <item> <value>
\tEx:\tconfig host_url http://www.example.com
''')
        elif params[0] == 'search':
            print('''\n\tThis command is used to search an exploit based on keywords. You
\tcan view the entire list by typing 'search' without argument.

\tUsage:\tsearch <keyword1> <keyword2> <...>
\tEx:\tsearch wordpress plugin
''')
        elif params[0] == 'show':
            print('''\n\tThis command is used to show the informations about an exploit
\t(author, description, configuration...).

\tUsage:\tshow <id>
\tEx:\tshow 112
''')
        elif params[0] == 'set':
            print('''\n\tEach exploit can contain special fields that you can edit (for example
\ta username, a password, an email adress...). This command is used to
\tchange these values.

\tUsage:\tset <id> <configuration> <value>
\tEx:\tset 112 username nico
''')
        elif params[0] == 'generate':
            print('''\n\tThis command is used to generate the HTML exploit. You can display it
\ton the screen by typing 'generate <id>' without other argument. You
\tcan also pass a filename to create a new file.

\tUsage:\tgenerate <id> <filename>
\tEx:\tgenerate 112 index.html
''')
        elif params[0] == 'update':
            print('''\n\tThis command is used to check if new exploits are available and update
\tthe exploits list if this is the case.

\tUsage:\tupdate
''')
        elif params[0] == 'help':
            print('''
        ,--.!,
     __/   -*-
   ,d08b.  '|`  IT MAKES NO SENSE !!
   0088MM
   `9MMP'
''')
        elif params[0] == 'clear':
            print('''\n\tThis command is used to clear the screen.

\tUsage:\tclear
''')
        elif params[0] == 'exit':
            print('''\n\tThis command is used to quit CSR2F.

\tUsage:\texit
''')
        else:
            om.error("This command does not exist")


class SearchCommand():

    def __init__(self):
        self.exploits_list = ExploitsManager().exploits
        self.exploits_list = OrderedDict(sorted(self.exploits_list.items(), key= lambda x: x[1]['date'], reverse=True))
        

    def run(self, params):
        print('''
\tDate           ID     Name                            Description
\t====           ==     ====                            ===========
''')

        for exploit_id, exploit in self.exploits_list.items():
            if params :
                try:
                    for param in params:
                        if (param.lower() not in exploit['name'].lower()) and (param.lower() not in exploit['description'].lower()):
                            raise ParamsNotExistsException
                except ParamsNotExistsException:
                    continue
                        

            description = str(exploit['description'])[:70] + "..." if len(exploit['description']) > 70 else exploit['description']
            description = description.replace('\n', ' ')
            name = str(exploit['name'])[:25].rstrip() + "..." if len(exploit['name']) > 25 else exploit['name']

            print("\t{:<15}{:<7}{:<32}{:<30}".format(exploit['date'],exploit_id, name, description))

        print("\t")


class UpdateCommand():

    def run(self, params):
        local_last_exploit = em.get_local_last_exploit()
        remote_last_exploit = em.get_remote_last_exploit()
        if remote_last_exploit == -1:
            om.error("You must install requests module to get the new exploits\n\n\t$ pip install requests\n")
            return None
        elif remote_last_exploit == -2:
            om.error("Error : A Connection error occurred")
            return None

        if int(local_last_exploit) == int(remote_last_exploit):
            om.info("The list of exploits is already updated")
            em.set_last_update()
        else:
            try:
                nb_exploits = em.update_exploits_list()
                exploits_str = "exploits" if nb_exploits > 1 else "exploit"
                om.info("{} new {} added".format(nb_exploits, exploits_str))
                om.info("Last update : {}".format(em.get_last_update()))
            except UpdateException:
                om.error("Error during exploits update")


class ExitCommand():

    def run(self, params):
        om.info('Bye')
        exit(0)


class GenerateCommand():

    def run(self, params):
        try:
            id_exploit = int(params[0])
        except (IndexError, ValueError, TypeError):
            om.error('You must specify an exploit id')
            return 0

        if em.find(int(id_exploit)) is None:
            om.error('This exploit does not exist')
        else:

            conf = config.config
            exploit = em.find(int(id_exploit))
            code = Generator(conf, exploit)

            try:
                filename = params[1]
            except IndexError:
                print("\n{}\n".format(code.get_page()))
                return 0
            else:
                if code.save_file(filename):
                    om.info("The file was created in 'output' folder")
                else:
                    om.error("A problem occured. Is that the file is writable ?")
                    print("\n{}\n".format(code.get_page()))


class SetCommand():

    def __init__(self):
        self.exploit = {}

    def run(self, params):
        try:
            id_exploit = int(params[0])
        except (IndexError, ValueError, TypeError):
            om.error('You must specify an exploit id')
            return 0

        try:
            name = params[1]
            value = " ".join(params[2:])
        except IndexError:
            om.error('You must specify a parameter name and a value')
            return 0

        self.exploit = em.find(int(id_exploit))
        if self.exploit is None:
            om.error('This exploit does not exist')
        else:
            for param in self.exploit['params']:
                try:
                    if param['name'] == name and param['custom'] == True:
                        param['user_value'] = value
                        om.info("The value has been modified")
                        return 0
                except KeyError:
                    pass
            om.error("This parameter doesn't exist")

class ShowCommand():

    def __init__(self):
        self.exploit = {}

    def run(self, params):

        try:
            id_exploit = int(params[0])
        except (IndexError, ValueError, TypeError):
            om.error('You must specify an exploit id')
            return 0

        self.exploit = em.find(int(id_exploit))
        if self.exploit is None:
            om.error('This exploit does not exist')
        else:

            author = 'Unknown' if not self.exploit['author'] else self.exploit['author']
            author_url = '' if not self.exploit['author_url'] else '('+self.exploit['author_url']+')'
            params = [p for p in self.exploit['params'] if p['custom'] == True]
            description = ""
            for line in self.exploit['description'].split('\n'):
                if line == '':
                    description += "\n"
                else:
                    words = line.split()
                    for i in range(0, len(words), 12):
                        description += "\t" + " ".join(words[i:i + 12]) + "\n"

            print('''
Informations
============

\tName : {} ({})
\t----

\tDescription
\t-----------
{}
\tAuthor : {} {}
\t------

\tMethod & Path : ({}) {}
\t-------------
'''.format(self.exploit['name'], self.exploit['date'], description, author, author_url, self.exploit['method'], self.exploit['path']))

            # print configuration paramters
            if params:
                print("Configuration\n=============\n")
                for p in params:
                    name = p['name']
                    try:
                        value = p['user_value']
                    except KeyError:
                     value = p['value']
                    t = len(name) * '-'
                    print('''\t{} => {}\n\t{}\n\t{}\n'''.format(name, value, t, p['description']))


class ClearCommand():

    def run(self, params):
        if os.name == "posix":
            os.system('clear')
        elif os.name in ("nt", "dos", "ce"):
            os.system('cls')
        else:
            om.error("This command is not supported by your system")



class ConfigCommand():

    def __init__(self):
        self.config = config.config

    def run(self, params):
        if not params:
            print('''
\tConfig\t\t\tValue
\t======\t\t\t=====
''')
            for key, value in list(self.config.items()):
                print("\t{}\t\t{}".format(key, value))
            print("\t")
        else:
            value = config.get(params[0])
            if value is not None:
                if len(params) >= 2:
                    config.set(params[0], params[1:])
                    om.info("The value has been modified")
                else:
                    print(" {} => {}".format(params[0], value))
            else:
                om.error("This config does not exist")



class CommandsManager:

    def __init__(self):
        self.cmds = {
                'exit': ExitCommand(),
                'clear': ClearCommand(),
                'generate': GenerateCommand(),
                'search': SearchCommand(),
                'set': SetCommand(),
                'show': ShowCommand(),
                'help': HelpCommand(),
                'update': UpdateCommand(),
                'config': ConfigCommand()
            }

    def find(self, cmd):
        if cmd in self.cmds:
            return self.cmds[cmd]
        else:
            raise CmdNotExistsException('unknown command (' + cmd + ')')

    def commands(self):
        return self.cmds.keys()
