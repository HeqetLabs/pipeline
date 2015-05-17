import datetime
from flask import request
from flask.ext.restful import Resource, abort

from pipeline import publisher

class Pipeline(Resource):
  def post(self, channel):
    #TODO: make this better
    publisher.conn.publish(channel, [request.get_data()])
