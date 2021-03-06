#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# sudo pelican --autoreload --listen

from string import Template
from datetime import date


AUTHOR = 'David Wolf'
SITENAME = 'David Wolf'
# SITENAME = 'Darksome'
SITEURL = 'http://localhost:8000'
# SITEURL = 'https://davidwolf.dev'

# PAGE_PATHS = ['pages']
STATIC_PATHS = ['CNAME', 'media']  # CNAME for GitHub Pages custom apex domain
# STATIC_EXCLUDES = ['sass']
IGNORE_FILES = ['_includes', '_*.*']

USE_FOLDER_AS_CATEGORY = False

PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = '{lang}/{slug}/index.html'
ARTICLE_URL = '{lang}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}/index.html'
ARTICLE_LANG_URL = '{lang}/{slug}/'
ARCHIVES_SAVE_AS = 'publications/index.html'
ARCHIVES_URL = 'publications/'
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHORS_URL = 'authors/'
AUTHOR_SAVE_AS = 'authors/{slug}/index.html'
AUTHOR_URL = 'authors/{slug}/'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAG_URL = 'tags/{slug}/'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = './docs'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d. %B 1%Y 𐅪'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
# DEFAULT_CATEGORY = None

MENUITEMS = (('publications', ARCHIVES_URL),)
DISPLAY_CATEGORIES_ON_MENU = False

THEME = '../pelican-theme-darksome'

PLUGINS = [
    'plugins.asciidoc_reader',
    # 'sitemap',
]
# ASCIIDOC_OPTIONS = ["-a source-highlighter=pygments"]
# https://pypi.org/project/pelican-sitemap/
SITEMAP = {
    "format": "xml",
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

"""theme specific settings below 👇"""


CANONICALURLS = (
    'http://www.david🐺.to',
    'https://davidwolf.dev',
    'https://www.davidwolf.dev',
)

"""not used on index"""
TITLE_SEPARATOR = '—'  # Title {{ TITLE_SEPARATOR }} Site Name

"""
decide which cards should be displayed on listing pages
available: 'categories', 'tags', 'authors'
"""
# SIDEBAR_CARDS = ('categories', 'tags', 'authors')
SIDEBAR_CARDS = ('tags')

# human era
FOOTERTEXT = 'Copyright © 12019 - {0}'.format(date.today().year + 10000)

"""links displayed in page footer"""
FOOTERITEMS = (
    ('Legal', 'legal/'),  # title, link (SITEURL will be added automaticly)
    ('Privacy', 'privacy/'),
    ('Feed', 'feed.xml'),
)

MEDIA = {
    'logo': 'media/images/logo.svg',
    'og-image': 'media/images/og-image.webp',
    'favicon': 'media/images/favicon.svg',
    'background': 'media/images/background.webp',  # on home
}

"""used wherever articles are listed"""
TRANSLATIONS = {
    'en': {
        'flag': '🇬🇧'
    },
    'de': {
        'flag': '🇩🇪'
    },
}

"""raw json-ld to insert on every site"""
with open('jsonld.json') as f:
    json = f.read()
t = Template(json)
JSON_LD = t.substitute(url=SITEURL)
