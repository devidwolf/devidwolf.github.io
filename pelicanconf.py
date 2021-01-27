#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import glob


LANDING_VIDEOS = [os.path.basename(path) for path in glob.glob('./content/media/videos/landing-*.webm')]

TITLE_SEPARATOR = '⁓'

# PAGE_PATHS = ['pages']
STATIC_PATHS = ['CNAME', 'media'] # CNAME for GitHub Pages
# STATIC_EXCLUDES = ['sass']

PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}/index.html'
ARTICLE_LANG_URL = '{lang}/{slug}/'

ARCHIVES_SAVE_AS = 'archives/index.html'
ARCHIVES_URL = 'archives/'
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHORS_URL = 'authors/'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories/'
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags/'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = './docs'

AUTHOR = 'David Wolf'
SITENAME = 'David Wolf'
# SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d. %B 1%Y HE'

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

# LINKS = (('PayPal.Me', 'https://paypal.me/devidwolf'),
# ('Buy me a coffee', 'https://buymeacoffee.com/dwolf'),)

# AFFILIATES = (
#             ('Get eco-friendly Web Hosting', 'green-hosting.svg', 'https://www.udmedia.de/r18841'),
#             ('Royalty-Free Stock Video at Pond5', 'pond5.webp', 'https://www.pond5.com/?ref=PlanetNine'),
#              )

DEFAULT_PAGINATION = False

THEME = './theme'

PLUGINS = [
    'plugins.asciidoc_reader',
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TRANSLATIONS = {
    'en': {
        'flag': '🇬🇧'
        },
    'de': {
        'flag': '🇩🇪'
        }
}
