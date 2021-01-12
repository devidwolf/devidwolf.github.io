#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import glob

LANDING_VIDEOS = [os.path.basename(path) for path in glob.glob('./content/videos/landing-*.webm')]

PAGE_PATHS = ['']
STATIC_PATHS = ['CNAME', 'images', 'videos', 'certificates']
# STATIC_EXCLUDES = ['sass']

PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = './docs'

AUTHOR = 'David Wolf'
SITENAME = 'David Wolf'
# SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
            ('GitHub', 'https://github.com/devidwolf'),
            ('SoloLearn', 'https://www.sololearn.com/Profile/15515516'),
            ('Codecademy', 'https://www.codecademy.com/profiles/764'),
         )

# Blogroll
# LINKS = (('PayPal.Me', 'https://paypal.me/devidwolf'),
# ('Buy me a coffee', 'https://buymeacoffee.com/dwolf'),)

AFFILIATES = (
            ('Get eco-friendly Web Hosting', 'green-hosting.svg', 'https://www.udmedia.de/r18841'),
             )

DEFAULT_PAGINATION = False

THEME = './theme'

# PLUGINS = [
#     'plugins.assets',
# ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
