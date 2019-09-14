#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Benny Daon'
SITENAME = u''
SITESUBTITLE = 'Building Fires in The Cloud'
SITEURL = ''

PATH = 'content'
THEME = 'theme/crowsfoot'

GITHUB_ADDRESS = 'https://github.com/daonb'
TWITTER_ADDRESS = 'https://twitter.com/daonb'
FB_ADDRESS = 'https://www.facebook.com/daonb'
LI_ADDRESS = 'https://il.linkedin.com/in/daonb'
FLICKR_ADDRESS = 'https://flickr.com/daonb'
PROFILE_IMAGE_URL = "/images/tuzig_logo.png"

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
             ('Me', '/pages/me.html'),
             ('Services', '/pages/services.html'),
             ('Bio', '/pages/bio.html'),
             ('Hacking Gov', '/pages/hacking-gov.html'),
             ('Colophone', '/pages/colophone.html'),
             )

DEFAULT_CATEGORY = 'blog'

TIME_ZONE = 'Asia/Jerusalem'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
'''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
'''

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
