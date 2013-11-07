from datetime import datetime
from django.utils.translation import pgettext, ugettext as _


__all__ = ("date", )


def date(time):

    now = datetime.now(time.tzinfo)

    if time > now:
        past = False
        diff = time - now
    else:
        past = True
        diff = now - time

    days = diff.days

    if days is 0:
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


def pluralization(n, quantity):
    #supports pl
    bits = quantity.split(',')
    if len(bits) > 3:
        bits = bits[0:3]
    elif len(bits) == 1:
        bits.append(bits[0])
        bits.append(bits[0])
    elif len(bits) == 2:
        bits.append(bits[1])

    if n==1:
        return bits[0]
    elif n%10>=2 and n%10<=4 and (n%100<10 or n%100>=20):
        return bits[1]
    else:
        return bits[2]


def _pretty_format(diff_amount, units, text, past):
    pretty_time = (diff_amount + units / 2) / units
    text = pluralization(pretty_time, text)
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
