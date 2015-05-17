import os
from flask import Flask
from flask.ext import restful

app = Flask(__name__)

app.config["REDIS_HOST"] = os.environ["REDIS_HOST"]
app.config["REDIS_PORT"] = os.environ["REDIS_PORT"]
app.config["REDIS_HEALTH_CHECK_CHANNEL"] = os.environ["REDIS_HEALTH_CHECK_CHANNEL"]
app.config["REDIS_ID"] = os.environ["REDIS_ID"]

api = restful.Api(app)

from .publisher import Publisher

publisher = Publisher(app)

from endpoints_v1 import Pipeline

api.add_resource(Pipeline, "/pipeline/v1/publish/<string:channel>")
