#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benny Daon'
SITENAME = u''
SITESUBTITLE = 'Starting fires in the clouds'
SITEURL = ''

PATH = 'content'
THEME = 'theme/crowsfoot'

GITHUB_ADDRESS = 'https://github.com/daonb'
TWITTER_ADDRESS = 'https://twitter.com/daonb'
FB_ADDRESS = 'https://www.facebook.com/daonb'
PROFILE_IMAGE_URL = "/images/tuzig_logo.png"

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
             ('Services', '/pages/services.html'),
             ('Philanthropy', '/pages/philanthropy.html'),
             ('About', '/pages/about.html'),
             )

TIME_ZONE = 'Asia/Jerusalem'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Open Knesset', 'http://oknesset.org/'),
         ('Hasadna', 'http://hasadna.org.il/'),
         ('PyWeb-IL', '#'),
        )

# Social widget
SOCIAL = (('discourse(he)', 'http://forum.hasadna.org.il/users/daonb'),
          ('twitter', 'https://twitter.com/daonb'),
          ('github', 'https://github.com/daonb'),
          ('linkedin', 'http://il.linkedin.com/in/daonb'),
          ('flickr', 'http://flickr.com/daonb'),
          ('facebook (he)', 'https://www.facebook.com/daonb'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
