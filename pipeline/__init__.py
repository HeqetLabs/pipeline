from flask import Flask
from flask.ext import restful

app = Flask(__name__)

api = restful.Api(app)

from .publisher import Publisher

publisher = Publisher(app)

from endpoints_v1 import Pipeline

api.add_resource(Pipeline, "/pipeline/v1/publish/<string:channel>")
