#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'José Aniceto'
SITENAME = 'Annotatio'
SITEURL = ''
BIO = 'A collection of codding notes and snippets from my journey of self taught programming.'
# PROFILE_IMAGE = 'photoB&W2_square.jpg'

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'
LOCALE = 'en_gb'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('user', 'joseaniceto.com'),)

# Social widget
SOCIAL = (('Personal Page', 'http://joseaniceto.com'),
          ('Github', 'https://github.com/jAniceto'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Custom settings
TYPOGRIFY = True
THEME = 'themes/pelican-hyde-2'
HYDE_THEME = 'theme-base-08'
USE_FOLDER_AS_CATEGORY = True
STATIC_PATHS = ['images']
USE_FOLDER_AS_CATEGORY = True
# ARTICLE_PATHS = ['']
SLUGIFY_SOURCE = 'basename'

# Debugging
LOAD_CONTENT_CACHE = False