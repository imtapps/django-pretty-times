from datetime import datetime
from django.utils.translation import pgettext, ugettext as _


__all__ = ("date", )


def get_now(time):
    return datetime.now(time.tzinfo)


def date(time):

    now = get_now(time)

    if time > now:
        past = False
        diff = time - now
    else:
        past = True
        diff = now - time

    days = abs(time.date() - now.date()).days

    if days is 0 or diff.total_seconds() < 60 * 60 * 24:
        return get_small_increments(diff.seconds, past)
    else:
        return get_large_increments(days, past)


def get_small_increments(seconds, past):
    if seconds < 10:
        result = _('just now')
    elif seconds < 60:
        result = _pretty_format(seconds, 1, _('seconds'), past)
    elif seconds < 120:
        result = past and _('a minute ago') or _('in a minute')
    elif seconds < 3600:
        result = _pretty_format(seconds, 60, _('minutes'), past)
    elif seconds < 7200:
        result = past and _('an hour ago') or _('in an hour')
    else:
        result = _pretty_format(seconds, 3600, _('hours'), past)
    return result


def get_large_increments(days, past):
    if days == 1:
        result = past and _('yesterday') or _('tomorrow')
    elif days < 7:
        result = _pretty_format(days, 1, _('days'), past)
    elif days < 14:
        result = past and _('last week') or _('next week')
    elif days < 31:
        result = _pretty_format(days, 7, _('weeks'), past)
    elif days < 61:
        result = past and _('last month') or _('next month')
    elif days < 365:
        result = _pretty_format(days, 30, _('months'), past)
    elif days < 730:
        result = past and _('last year') or _('next year')
    else:
        result = _pretty_format(days, 365, _('years'), past)
    return result


def _pretty_format(diff_amount, units, text, past):
    pretty_time = (diff_amount + units / 2) / units
    if past:
        base = pgettext(
            'Moment in the past',
            "%(amount)d %(quantity)s ago"
        )
    else:
        base = pgettext(
            'Moment in the future',
            "in %(amount)d %(quantity)s"
        )
    return base % dict(amount=pretty_time, quantity=text)
