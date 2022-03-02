import json


def load_config():
    with open('config/app_config.json', 'r') as f:
        config = json.load(f)
    return config


CONFIG = load_config()

PORT = CONFIG["API"]["PORT"]
PROD_ENDPOINT = CONFIG["APT"]["ROUTE"]["PROD_CONFIG"]
DEV_ENDPOINT = CONFIG["APT"]["ROUTE"]["DEV_CONFIG"]
