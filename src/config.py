import json


def load_config():
    with open('config/app_config.json', 'r') as f:
        config = json.load(f)
    return config


CONFIG = load_config()
HOST = CONFIG["API"]["HOST"]
PORT = CONFIG["API"]["PORT"]
PROD_ENDPOINT = CONFIG["API"]["ROUTE"]["PROD_CONFIG"]
DEV_ENDPOINT = CONFIG["API"]["ROUTE"]["DEV_CONFIG"]
