#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
python manage.py makemigrations budget
python manage.py makemigrations classification
python manage.py makemigrations file
python manage.py makemigrations product
python manage.py makemigrations accountOperations
python manage.py makemigrations family
python manage.py makemigrations
python manage.py migrate budget
python manage.py migrate classification
python manage.py migrate file
python manage.py migrate product
python manage.py migrate accountOperations
python manage.py migrate family
python manage.py migrate

"""