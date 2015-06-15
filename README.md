# gaesentry
getsentry integration for Google Appengine

## Important Requirement

Download and include the following modified raven-python code in your appengine project. Ensure that the name of the directory is `raven` and NOT `raven-python`. If the name of the directory is `raven-python`, rename it to `raven`.

https://github.com/albertpadin/raven-python


## Installation Instructions

Add the following lines to `appengine_config.py`:

```
def webapp_add_wsgi_middleware(app):

    import gaesentry
    gaesentry.add_sentry_to_logging()
    
    return app
```

If you already have a `webapp_add_wsgi_middleware` method, then simply insert the following lines within it:

```
import gaesentry
gaesentry.add_sentry_to_logging()
```
