import os
from raven import Client
from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging
import logging


def add_sentry_to_logging(dsn):
    if not os.environ.get('HTTP_HOST').startswith('localhost:'):
        # Configure the default client
        client = Client(dsn)
        handler = SentryHandler(client=client, level=logging.WARNING)
        setup_logging(handler)

