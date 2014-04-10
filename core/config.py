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

import json


class ConfigManager:

    def __init__(self):
        self.config = {}
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                self.config = json.load(f)
        except IOError:
            om.error("Error during import configuration file")

    def get(self, item):
        try:
            return self.config[item]
        except KeyError:
            return None

    def set(self, item, value):
        # just for title, authorize multiple values
        if item == "html_title":
            value = " ".join(value)
        else:
            value = value[0]

        self.config[item] = value
        try:
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=2)
                return True
        except IOError:
            om.error("Error during the configuration saving")
            return False
