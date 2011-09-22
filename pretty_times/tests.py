
from django.utils import unittest

from django.template import Template, Context
from pretty_times import pretty

from datetime import datetime, timedelta

import operator

class PrettyTimeTests(unittest.TestCase):

    def get_past_result(self, **kwargs):
        return self.get_result(operator.sub, **kwargs)

    def get_future_result(self, **kwargs):
        #because the gap between now and the future is rapidly closing
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

    def test_ten_seconds_ago(self):
        self.assertEqual("10 seconds ago", self.get_past_result(seconds=10))

    def test_in_ten_seconds(self):
        self.assertEqual("in 10 seconds", self.get_future_result(seconds=10))

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

    def test_tomorrow(self):
        self.assertEqual("tomorrow", self.get_future_result(days=1))

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
