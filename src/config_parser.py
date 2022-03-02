import json


def get_base_config():
    with open('config/base_config.json', 'r') as f:
        base_config = json.load(f)
    return {"main_config": base_config}


def get_dev_config():
    with open('config/dev_config.json', 'r') as f:
        dev_config = json.load(f)
    return {"dev_config": dev_config}


def get_prod_config():
    with open('config/prod_config.json', 'r') as f:
        prod_config = json.load(f)
    return {"prod_config": prod_config}
