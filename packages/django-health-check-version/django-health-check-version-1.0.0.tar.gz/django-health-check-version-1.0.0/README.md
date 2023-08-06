# django-health-check-version

A simple plugin that displays the `VERSION` value configured in `settings.py` in the output of `python manage.py health_check` or the `/health/` endpoint of the application.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django-health-check-version
```

Add `VERSION` to `settings.py` set to whatever value you wish displayed.

```python
VERSION='1.0.0'
```

Add to `INSTALLED_APPS` in `settings.py`

```python
INSTALLED_APPs = [
    ...
    "health_check",  # required
    "health_check.db",  # standard health checkers
    "health_check.cache",
    "health_check.storage",
    "health_check.contrib.migrations",
    "django_health_check_version", # this one
    ...
]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
