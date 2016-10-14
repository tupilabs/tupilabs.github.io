#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import json, requests
from jinja2 import Template
import datetime
import time
import re

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# TODO: add source
def is_valid_url(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)

# http://stackoverflow.com/questions/1820336/tokenize-a-string-keeping-delimiters-in-python
def urlify(text):
    t = ''
    splitter = re.compile(r'(\s+|\S+|,|\.|\n|:|;)')
    for token in splitter.findall(text):
        if (is_valid_url(token)):
            t += "[" + token + "](" + token + ")"
        else:
            t += token
    return t

# From: http://www.protocolostomy.com/2010/07/06/python-date-manipulation/
def get_last_whole_week(today=None, epoch=False):
    # a date object
    date_today = today or datetime.date.today()
    print("date_today: ", date_today)
 
    # By default day 0 is Monday. Sunday is 6.
    dow_today = date_today.weekday()
    print("dow_today: ", dow_today)
 
    if dow_today == 6:
        days_ago_saturday = 1
    else:
        # If day between 0-5, to get last saturday, we need to go to day 0 (Monday), then two more days.
        days_ago_saturday = dow_today + 2
    print("days_ago_saturday: ", days_ago_saturday)
    # Make a timedelta object so we can do date arithmetic.
    delta_saturday = datetime.timedelta(days=days_ago_saturday)
    print("delta_saturday: ", delta_saturday)
    # saturday is now a date object representing last saturday
    saturday = date_today - delta_saturday
    print("saturday: ", saturday)
    # timedelta object representing '6 days'...
    delta_prevsunday = datetime.timedelta(days=6)
    # Making a date object. Subtract the 6 days from saturday to get "the Sunday before that".
    prev_sunday = saturday - delta_prevsunday
 
    # we need to return a range starting with midnight on a Sunday, and ending w/ 23:59:59 on the
    # following Saturday... optionally in epoch format.
 
    if epoch:
        # saturday is date obj = 'midnight saturday'. We want the last second of the day, not the first.
        saturday_epoch = time.mktime(saturday.timetuple()) + 86399
        prev_sunday_epoch = time.mktime(prev_sunday.timetuple())
        last_week = (prev_sunday_epoch, saturday_epoch)
    else:
        saturday_str = saturday.strftime('%d-%b')
        prev_sunday_str = prev_sunday.strftime('%d-%b')
        last_week = (prev_sunday_str, saturday_str)
    return last_week

url = os.environ.get('TRELLO_URL_1')

params = dict()

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

tasks = list()

for d in data:
    tasks.append(urlify(d['name']))

if (len(tasks) > 0):
    today = datetime.datetime.today()
    #today = datetime.datetime(2014, 12, 1)
    dates = get_last_whole_week(today)
    from_date = dates[0]
    to_date = dates[1]
    time = time.strftime("%H:%M:%S", time.gmtime(666))

    file = open('template.tpl', 'r')
    template = Template(file.read())
    content = template.render({'from': from_date, 'to': to_date, 'time': time, 'author': 'kinow', 'tasks': tasks})

    file_name = today.strftime("%Y-%m-%d_tupilabs-report-" + from_date + "-" + to_date + ".html").lower()

    output_file = open(file_name, 'w')
    output_file.write(content)
    output_file.close()

    print('Report generated, archiving cards!')

    url = os.environ.get('TRELLO_URL_2')

    params = dict()

    resp = requests.post(url=url, params=params)

    #print resp.text

    print("All cards archived!")
else:
    print("No tasks since last report!")

