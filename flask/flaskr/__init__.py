import os

from flask import Flask , jsonify

from flask_cors import CORS 

import pandas as pd



# def create_app(test_config=None):
#     # create and configure the app
app = Flask(__name__, instance_relative_config=True)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_mapping(
    SECRET_KEY='dev',
)


from . import db
db.init_app(app)

from . import auth
app.register_blueprint(auth.bp)

from . import route
app.register_blueprint(route.bp)

@app.route("/")
def hello():
    return jsonify({"h":"hello world"})

