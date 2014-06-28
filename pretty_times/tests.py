import operator
from datetime import datetime, timedelta, tzinfo

import mock
from django.utils import unittest
from django.utils import translation
from django.template import Template, Context

from pretty_times import pretty


class PrettyTimeTests(unittest.TestCase):

    def get_past_result(self, **kwargs):
        return self.get_result(operator.sub, **kwargs)

    def get_future_result(self, **kwargs):
        # because the gap between now and the future is rapidly closing
        if 'seconds' in kwargs:
            kwargs['seconds'] += 1
        else:
            kwargs['seconds'] = 1

        return self.get_result(operator.add, **kwargs)

    def get_result(self, op, **kwargs):
        my_datetime = op(datetime.today(), timedelta(**kwargs))
        return self.apply_prettytime(my_datetime)

    def apply_prettytime(self, my_datetime):
        return pretty.date(my_datetime)

    def test_now(self):
        self.assertEqual("just now", self.apply_prettytime(datetime.today()))

    def test_now_tz(self):
        """test that non-naive datetimes are handled"""

        class UTC(tzinfo):
            """based on example tzinfo classes from:
            http://docs.python.org/release/2.5.2/lib/datetime-tzinfo.html
            """
            def utcoffset(self, dt):
                return timedelta(0)

            def dst(self, dt):
                return timedelta(0)

        dt = datetime.utcnow().replace(tzinfo=UTC())
        self.assertEqual("just now", self.apply_prettytime(dt))

    def test_ten_seconds_ago(self):
        self.assertEqual("10 seconds ago", self.get_past_result(seconds=10))

    def test_in_ten_seconds(self):
        self.assertEqual("in 10 seconds", self.get_future_result(seconds=10))

    def test_french_in_ten_second(self):
        try:
            translation.activate('fr')
            self.assertEqual("dans 10 secondes", self.get_future_result(seconds=10))
        finally:
            translation.activate('en')

    def test_french_ten_seconds_ago(self):
        try:
            translation.activate('fr')
            self.assertEqual("il y a 10 secondes", self.get_past_result(seconds=10))
        finally:
            translation.activate('en')

    def test_thirty_seconds_ago(self):
        self.assertEqual("30 seconds ago", self.get_past_result(seconds=30))

    def test_in_thirty_seconds(self):
        self.assertEqual("in 30 seconds", self.get_future_result(seconds=30))

    def test_one_minute_ago(self):
        self.assertEqual("a minute ago", self.get_past_result(minutes=1))

    def test_in_one_minute(self):
        self.assertEqual("in a minute", self.get_future_result(minutes=1))

    def test_two_minutes_ago(self):
        self.assertEqual("2 minutes ago", self.get_past_result(minutes=2))

    def test_in_two_minutes(self):
        self.assertEqual("in 2 minutes", self.get_future_result(minutes=2))

    def test_one_hour_ago(self):
        self.assertEqual("an hour ago", self.get_past_result(hours=1))

    def test_in_one_hour(self):
        self.assertEqual("in an hour", self.get_future_result(hours=1))

    def test_two_hours_ago(self):
        self.assertEqual("2 hours ago", self.get_past_result(hours=2))

    def test_in_two_hours(self):
        self.assertEqual("in 2 hours", self.get_future_result(hours=2))

    def test_yesterday(self):
        self.assertEqual("yesterday", self.get_past_result(days=1))

    @mock.patch('pretty_times.pretty.get_now')
    def test_dates_used_for_time_and_now_returns_in_two_days(self, get_now):
        get_now.return_value = datetime(2013, 5, 27, 11, 18)
        future_date = datetime(2013, 5, 29, 3, 15)
        self.assertEqual("in 2 days", pretty.date(future_date))

    @mock.patch('pretty_times.pretty.get_now')
    def test_in_hours_when_less_than_24_hours(self, get_now):
        get_now.return_value = datetime(2013, 5, 27, 11, 18)
        future_date = datetime(2013, 5, 28, 10, 15)
        self.assertEqual("in 23 hours", pretty.date(future_date))

    @mock.patch('pretty_times.pretty.get_now')
    def test_tomorrow_when_more_than_24_hours(self, get_now):
        get_now.return_value = datetime(2013, 5, 27, 11, 18)
        future_date = datetime(2013, 5, 28, 11, 19)
        self.assertEqual("tomorrow", pretty.date(future_date))

    def test_tomorrow(self):
        self.assertEqual("tomorrow", self.get_future_result(days=1))

    def test_next_week(self):
        self.assertEqual("next week", self.get_future_result(days=8))

    def test_two_weeks_ago(self):
        self.assertEqual("2 weeks ago", self.get_past_result(days=15))

    def test_in_two_weeks(self):
        self.assertEqual("in 2 weeks", self.get_future_result(days=15))

    def test_last_week(self):
        self.assertEqual("last week", self.get_past_result(days=8))

    def test_two_days_ago(self):
        self.assertEqual("2 days ago", self.get_past_result(days=2))

    def test_in_two_days(self):
        self.assertEqual("in 2 days", self.get_future_result(days=2))

    def test_three_days_ago(self):
        self.assertEqual("3 days ago", self.get_past_result(days=3))

    def test_in_three_days(self):
        self.assertEqual("in 3 days", self.get_future_result(days=3))

    def test_last_month(self):
        self.assertEqual("last month", self.get_past_result(days=32))

    def test_next_month(self):
        self.assertEqual("next month", self.get_future_result(days=32))

    def test_two_months_ago(self):
        self.assertEqual("2 months ago", self.get_past_result(days=63))

    def test_in_two_months(self):
        self.assertEqual("in 2 months", self.get_future_result(days=63))

    def test_last_year(self):
        self.assertEqual("last year", self.get_past_result(days=366))

    def test_next_year(self):
        self.assertEqual("next year", self.get_future_result(days=366))

    def test_two_years_ago(self):
        self.assertEqual("2 years ago", self.get_past_result(days=733))

    def test_in_two_years(self):
        self.assertEqual("in 2 years", self.get_future_result(days=733))


class PrettyTimeTemplateTagTests(PrettyTimeTests):

    def apply_prettytime(self, my_datetime):
        template = Template("""
        {% load prettytimes_tags %}
        {{ my_datetime|relative_time }}
        """)
        return template.render(Context(dict(my_datetime=my_datetime))).strip()
