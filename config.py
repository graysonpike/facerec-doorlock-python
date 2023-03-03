import json


CONFIG = None


def get_config():
    global CONFIG
    if not CONFIG:
        file = open('config.json')
        CONFIG = json.load(file)
    return CONFIG