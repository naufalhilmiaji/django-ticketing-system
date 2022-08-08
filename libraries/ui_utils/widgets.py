"""
Extra HTML Widget classes
"""

import datetime
import re

from django.forms.widgets import Widget, Select, TextInput, DateInput, DateTimeInput, TimeInput
from django.utils.dates import MONTHS
from django.utils.safestring import mark_safe
from django.utils.html import escape


class EmailInput(TextInput):
    input_type = 'email'


class URLInput(TextInput):
    input_type = 'url'


class NumberInput(TextInput):
    input_type = 'number'


class TelephoneInput(TextInput):
    input_type = 'tel'


class DateInput(DateInput):
    input_type = 'date'


class DateTimeInput(DateTimeInput):
    input_type = 'datetime'


class TimeInput(TimeInput):
    input_type = 'time'


RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')


class SelectDateWidget(Widget):
    """
    A Widget that splits date input into three <select> boxes.

    This also serves as an example of a Widget that has more than one HTML
    element and hence implements value_from_datadict.
    """
    none_value = (0, '---')
    month_field = '%s_month'
    day_field = '%s_day'
    year_field = '%s_year'

    def __init__(self, attrs=None, years=None, required=True):
        # years is an optional list/tuple of years to use in the "year" select box.
        self.attrs = attrs or {}
        self.required = required
        if years:
            self.years = years
        else:
            this_year = datetime.date.today().year
            self.years = range(this_year, this_year + 10)

    def render(self, name, value, attrs=None, renderer=None):
        try:
            year_val, month_val, day_val = value.year, value.month, value.day
        except AttributeError:
            year_val = month_val = day_val = None
            if isinstance(value, str):
                match = RE_DATE.match(value)
                if match:
                    year_val, month_val, day_val = [int(v) for v in match.groups()]

        output = []

        if 'id' in self.attrs:
            id_ = self.attrs['id']
        else:
            id_ = 'id_%s' % name

        day_choices = [(i, i) for i in range(1, 32)]
        if not (self.required and value):
            day_choices.insert(0, self.none_value)
        local_attrs = self.build_attrs(
            {'id': self.day_field % id_})

        s = Select(choices=day_choices)
        select_html = s.render(self.day_field % name, day_val, local_attrs)
        output.append(select_html)

        month_choices = list(MONTHS.items())
        if not (self.required and value):
            month_choices.append(self.none_value)
        month_choices.sort()
        local_attrs['id'] = self.month_field % id_

        s = Select(choices=month_choices)
        select_html = s.render(self.month_field % name, month_val, local_attrs)
        output.append(select_html)

        year_choices = [(i, str(i)) for i in self.years]
        if not (self.required and value):
            year_choices.insert(0, self.none_value)
        local_attrs['id'] = self.year_field % id_
        s = Select(choices=year_choices)
        select_html = s.render(self.year_field % name, year_val, local_attrs)
        output.append(select_html)

        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        return '%s_month' % id_
    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        d = data.get(self.day_field % name)
        if y == m == d == "0":
            return None
        if y and m and d:
            return '%s-%s-%s' % (y, m, d)
        return data.get(name, None)


RE_DATETIME = re.compile(r'(\d{4})-(\d\d?)-(\d\d?) (\d\d?):(\d\d?)$')


class SelectDatetimeWidget(SelectDateWidget):
    """
    A Widget that splits date input into five <select> boxes.
    """

    hour_field = '%s_hour'
    minute_field = '%s_minute'

    def render(self, name, value, attrs=None, renderer=None):
        try:
            year_val, month_val, day_val, hour_val, minute_val = (value.year,
                                                                  value.month,
                                                                  value.day,
                                                                  value.hour,
                                                                  value.minute)
        except AttributeError:
            year_val = month_val = day_val = hour_val = minute_val = None
            if isinstance(value, str):
                match = RE_DATETIME.match(value)
                if match:
                    year_val, month_val, day_val, hour_val, minute_val = [int(v) for v in match.groups()]

        output = []

        if 'id' in self.attrs:
            id_ = self.attrs['id']
        else:
            id_ = 'id_%s' % name

        day_choices = [(i, i) for i in range(1, 32)]
        if not (self.required and value):
            day_choices.insert(0, self.none_value)
        local_attrs = self.build_attrs({'id': self.day_field % id_})

        s = Select(choices=day_choices)
        select_html = s.render(self.day_field % name, day_val, local_attrs)
        output.append(select_html)
        month_choices = list(MONTHS.items())
        if not (self.required and value):
            month_choices.append(self.none_value)
        month_choices.sort()
        local_attrs['id'] = self.month_field % id_

        s = Select(choices=month_choices)
        select_html = s.render(self.month_field % name, month_val, local_attrs)
        output.append(select_html)

        year_choices = [(i, i) for i in self.years]
        if not (self.required and value):
            year_choices.insert(0, self.none_value)
        local_attrs['id'] = self.year_field % id_
        s = Select(choices=year_choices)
        select_html = s.render(self.year_field % name, year_val, local_attrs)
        output.append(select_html)
        output.append("&nbsp; &nbsp;")
        hour_choices = [(i, "%02d" % i) for i in range(0, 24)]
        if not (self.required and value):
            hour_choices.insert(0, self.none_value)
        local_attrs = self.build_attrs({'id': self.hour_field % id_})

        s = Select(choices=hour_choices)
        select_html = s.render(self.hour_field % name, hour_val, local_attrs)
        output.append(select_html)
        output.append(":")
        minute_choices = [(i, "%02d" % i) for i in range(0, 60, 10)]
        if not (self.required and value):
            minute_choices.insert(0, self.none_value)
        local_attrs = self.build_attrs({'id': self.minute_field % id_})

        s = Select(choices=minute_choices)
        select_html = s.render(self.minute_field % name, minute_val, local_attrs)
        output.append(select_html)

        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        return '%s_month' % id_
    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        d = data.get(self.day_field % name)

        hour = data.get(self.hour_field % name)
        minute = data.get(self.minute_field % name)

        if y == m == d == hour == minute == "0":
            return None
        if y and m and d and hour and minute:
            return '%s-%s-%s %s:%s' % (y, m, d, hour, minute)
        return data.get(name, None)