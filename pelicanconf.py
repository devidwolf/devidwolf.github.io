#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PAGE_PATHS = ['']
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

# Blogroll
LINKS = (('GitHub', 'https://github.com/devidwolf'),
         ('PayPal.Me', 'https://paypal.me/devidwolf'),
         ('Buy me a coffee', 'https://buymeacoffee.com/dwolf'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

THEME = './theme'

PLUGINS = [
    'plugins.assets',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
