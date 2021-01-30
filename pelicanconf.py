#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'David Wolf'
SITENAME = 'David Wolf'
# SITENAME = 'Darksome'
# SITEURL = 'http://localhost:8000'

# PAGE_PATHS = ['pages']
STATIC_PATHS = ['CNAME', 'media'] # CNAME for GitHub Pages custom apex domain
# STATIC_EXCLUDES = ['sass']
IGNORE_FILES = ['_includes']

# USE_FOLDER_AS_CATEGORY = False

PAGE_SAVE_AS            = '{slug}/index.html'
PAGE_URL                = '{slug}/'
ARTICLE_PATHS           = ['posts']
ARTICLE_SAVE_AS         = '{slug}/index.html'
ARTICLE_URL             = '{slug}/'
ARTICLE_LANG_SAVE_AS    = '{lang}/{slug}/index.html'
ARTICLE_LANG_URL        = '{lang}/{slug}/'
ARCHIVES_SAVE_AS        = 'archives/index.html'
ARCHIVES_URL            = 'archives/'
AUTHORS_SAVE_AS         = 'authors/index.html'
AUTHORS_URL             = 'authors/'
AUTHOR_SAVE_AS          = 'authors/{slug}/index.html'
AUTHOR_URL              = 'authors/{slug}/'
CATEGORIES_SAVE_AS      = 'categories/index.html'
CATEGORIES_URL          = 'categories/'
CATEGORY_SAVE_AS        = 'categories/{slug}/index.html'
CATEGORY_URL            = 'categories/{slug}/'
TAGS_SAVE_AS            = 'tags/index.html'
TAGS_URL                = 'tags/'
TAG_SAVE_AS             = 'tags/{slug}/index.html'
TAG_URL                 = 'tags/{slug}/'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = './docs'

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

DEFAULT_PAGINATION = False

MENUITEMS = (('publications', ARCHIVES_URL),)
DISPLAY_CATEGORIES_ON_MENU = False

THEME = '../pelican-theme-darksome'

PLUGINS = [
    'plugins.asciidoc_reader',
]
ASCIIDOC_OPTIONS = ["-a source-highlighter=pygments"]


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

"""theme specific settings below 👇"""

from datetime import date

FOOTERTEXT = 'Copyright © 12019 - {0}'.format(date.today().year + 10000) # human era

"""links displayed in page footer"""
FOOTERITEMS = (
    ('legal', 'legal/'), # title, link (SITEURL will be added automaticly)
    ('privacy', 'privacy/'),
)

"""not used on index"""
TITLE_SEPARATOR = '-' # Title - Site Name

MEDIA = {
    'logo': 'media/images/logo.svg',
    'favicon': 'media/images/favicon.svg',
    'background': 'media/images/background.webp', # on home
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
