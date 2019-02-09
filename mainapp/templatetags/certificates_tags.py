from django import template
from django.template.defaultfilters import stringfilter
import datetime

register = template.Library()

@stringfilter
@register.filter(name='notoverdue')
def notoverdue(date):
    year, month, day = str(date).split('-')
    cert_valid_end = datetime.datetime(int(year), int(month), int(day))
    now_date = datetime.datetime.now()
    time_delta = cert_valid_end - now_date
    result, *_ = str(time_delta).split(' ')
    seconds = time_delta.total_seconds()
    hours = seconds // 3600
    if hours <= 0:
        return True
    else:
        return False

@stringfilter
@register.filter(name='notoverdue_add_td_tag')
def notoverdue_add_td_tag(date):
    year, month, day = str(date).split('-')
    cert_valid_end = datetime.datetime(int(year), int(month), int(day))
    now_date = datetime.datetime.now()
    time_delta = cert_valid_end - now_date
    result, *_ = str(time_delta).split(' ')
    seconds = time_delta.total_seconds()
    hours = seconds // 3600
    if hours <= 0:
        return 'class=table-danger'
    if 2720 > hours > 0:
        return 'class=table--warning'
    else:
        return 'class=table-success'

#@register.filter(name='notoverdue')
@stringfilter
@register.tag
def notoverdue_tag (date):
    year, month, day = date.split('-')
    cert_valid_end = datetime.datetime(int(year), int(month), int(day))
    now_date = datetime.datetime.now()
    time_delta = cert_valid_end - now_date
    result, *_ = str(time_delta).split(' ')
    seconds = time_delta.total_seconds()
    hours = seconds // 3600
    if hours >= 0:
        return True
    else:
        return False
