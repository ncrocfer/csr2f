#/usr/bin/python3
# -*- coding: utf-8 -*-

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
