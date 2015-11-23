"""
WSGI config for django_example_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os
import static

SETTINGS_MODULE = "django_example_app.settings." + \
    os.environ.get('ENVIRONMENT', 'production')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)


from django.core.wsgi import get_wsgi_application


class Dispatcher(object):
    """
    Dispatches requests between two WSGI apps, a static file server and a
    Django server.
    """

    def __init__(self):
        self.django_handler = get_wsgi_application()
        self.static_handler = static.Cling(
            os.path.dirname(os.path.dirname(__file__)))

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'].startswith('/static'):
            return self.static_handler(environ, start_response)
        else:
            return self.django_handler(environ, start_response)

application = Dispatcher()

# Wrap werkzeug debugger if DEBUG is on
from django.conf import settings
if settings.DEBUG:
    try:
        import django.views.debug
        import six
        from werkzeug.debug import DebuggedApplication

        def null_technical_500_response(request, exc_type, exc_value, tb):
            six.reraise(exc_type, exc_value, tb)

        django.views.debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True)
    except ImportError:
        pass
