import json
import logging
import redis

from flask import current_app
from flask import _app_ctx_stack as stack

LOG = logging.getLogger("Publisher")

class Publisher(object):

  def __init__(self, app=None):
    self.app = app

    if self.app is not None:
      self.init_app(app)

  def init_app(self, app):
    app.config.setdefault("REDIS_HOST", "127.0.0.1")
    app.config.setdefault("REDIS_PORT", 6379)
    app.config.setdefault("REDIS_HEALTH_CHECK_CHANNEL", "health-check-channel")
    app.config.setdefault("REDIS_ID", "publisher")

  @property
  def conn(self):
    ctx = stack.top

    if ctx is not None:
      if not hasattr(ctx, 'publisher'):
        r = redis.StrictRedis(host=current_app.config["REDIS_HOST"], port=current_app.config["REDIS_PORT"])
        LOG.info("Started Publisher")
        r.publish(current_app.config["REDIS_HEALTH_CHECK_CHANNEL"], "OK")
        ctx.publisher = r
      return ctx.publisher

  def publish(self, channel, batch):
    LOG.info("Sending %d messages on %s channel" % (len(batch), channel))
    for b in batch:
      self.r.publish(channel, json.dumps(b))

