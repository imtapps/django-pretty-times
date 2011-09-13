Almost all of this was borrowed from the py-pretty library,
tested then refactored.

py-pretty Functionaility
========================
::

    >>> from datetime import datetime, timedelta
    >>> from pretty_times import pretty
    >>> now = datetime.now()
    >>> pretty.date(now)
    'now'
    >>> pretty.date(now - timedelta(seconds=30))
    '30 seconds ago'
    >>> pretty.date(now + timedelta(seconds=31))
    'in 30 seconds'
    >>> pretty.date(now - timedelta(minutes=1))
    'a minute ago'
    >>> pretty.date(now + timedelta(minutes=1, seconds=1))
    'in a minute'
    >>> pretty.date(now - timedelta(hours=1))
    'an hour ago'
    >>> pretty.date(now + timedelta(hours=1, seconds=1))
    'in an hour'
    >>> pretty.date(now - timedelta(days=1))
    'yesterday'
    >>> pretty.date(now + timedelta(days=1, seconds=1))
    'tomorrow'
    >>> pretty.date(now - timedelta(days=2))
    '2 days ago'
    >>> pretty.date(now + timedelta(days=2, seconds=1))
    'in 2 days'
    >>> pretty.date(now - timedelta(days=9))
    'last week'
    >>> pretty.date(now + timedelta(days=9, seconds=1))
    'next week'
    >>> pretty.date(now - timedelta(days=16))
    '2 weeks ago'
    >>> pretty.date(now + timedelta(days=16, seconds=1))
    'in 2 weeks'
    >>> pretty.date(now - timedelta(days=32))
    'last month'
    >>> pretty.date(now + timedelta(days=32, seconds=1))
    'next month'
    >>> pretty.date(now - timedelta(days=64))
    '2 months ago'
    >>> pretty.date(now + timedelta(days=64, seconds=1))
    'in 2 months'
    >>> pretty.date(now - timedelta(days=367))
    'last year'
    >>> pretty.date(now + timedelta(days=367, seconds=1))
    'next year'
    >>> pretty.date(now - timedelta(days=735))
    '2 years ago'
    >>> pretty.date(now + timedelta(days=735, seconds=1))
    'in 2 years'


Django Integration
==================
::

    {% load prettytimes_tags %}
    {{ my_datetime|relative_time }}

