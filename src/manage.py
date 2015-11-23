#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # CHANGED manage.py will use development settings by
    # default. Change the DJANGO_SETTINGS_MODULE environment variable
    # for using the environment specific settings file.
    SETTINGS_MODULE = "django_example_app.settings." + \
        os.environ.get('ENVIRONMENT', 'production')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
