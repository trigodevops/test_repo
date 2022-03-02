import json

import flask

from src.config_parser import get_base_config, get_dev_config, get_prod_config

app = flask.Flask(__name__)

base_config = get_base_config()


@app.route('/prod/config/', methods=['GET'])
def expose_prod_config():
    prod_config = get_prod_config()
    exposed_config = {**base_config, **prod_config}
    return json.dumps(exposed_config)


@app.route('/dev/config/', methods=['GET'])
def expose_dev_config():
    dev_config = get_dev_config()
    exposed_config = {**base_config, **dev_config}
    return json.dumps(exposed_config)


app.run()
