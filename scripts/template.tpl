---
title: 'TupiLabs Report: {{ from }}, {{ to }}'
author: {{ author }}
tags:
    - tupilabs-report
time: '{{ time }}'
category: news
layout: blog
---
This is our weekly Open Source report with news from {{ from }} to {{ to }}. 

{% for task in tasks %}
- {{ task }}
{% endfor %}

We are working [for you](http://tupilabs.com/for_you/)

Have a great week! :-)
