import os
from raven import Client
from raven.handlers.logging import SentryHandler
from raven.conf import setup_logging
import logging


GAESENTRY_SENTRY_DSN = ''  # get this from getsentry. Use the "sync+https://" prefix, and not "https://".


def add_sentry_to_logging():
    if not os.environ.get('HTTP_HOST').startswith('localhost:'):
        # Configure the default client
        client = Client(GAESENTRY_SENTRY_DSN)
        handler = SentryHandler(client=client, level=logging.WARNING)
        setup_logging(handler)

