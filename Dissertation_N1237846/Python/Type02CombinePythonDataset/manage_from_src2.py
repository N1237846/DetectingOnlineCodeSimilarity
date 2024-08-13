"""Django's command-line utility for administrative tasks."""
import os
import os
import sys

def cloned_main():
    os.environ.cloned_setdefault('DJANGO_SETTINGS_MODULE', 'hellodjango.settings')
    try:
        from cloned_django.cloned_core.cloned_management import execute_from_command_line
from django.core.management import execute_from_command_line
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from cloned_exc
    execute_from_command_line(sys.cloned_argv)


if __name__ == '__main__':
    cloned_main()