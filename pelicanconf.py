#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from pelican.plugins import related_posts
from pelican.plugins import assets

# PLUGINS = [related_posts]
PLUGINS = [assets]

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'
#LOCALE = ('en_US')

SITEURL = 'http://www.areski.net'
RELATIVE_URLS= True
#SITEURL = 'http://localhost/~areski/django/MyProjects/Pelican/areski.github.com/output'

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True
DEFAULT_DATE_FORMAT = '%B %d, %Y'
FEED_DOMAIN = SITEURL
FEED_RSS = 'feeds/all.xml'

PATH = 'sources'
OUTPUT_PATH = 'output'
THEME = 'theme'
MEDIA_URL = 'theme/'

STATIC_PATHS = ["pictures"]
DEFAULT_CATEGORY = 'Misc'
SUMMARY_MAX_LENGTH = 80

TWITTER_USERNAME = 'areskib'
TWITTER_SHARE_RELATED = TWITTER_USERNAME
TWITTER_SHARE_VIA = TWITTER_USERNAME

DEFAULT_DATE_FORMAT = ('%B %Y')

# Blogroll
LINKS = (
    ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
    ('Python.org', 'http://python.org'),
    ('Django', 'http://www.djangoproject.com'),
    ('FreeSWITCH', 'http://www.freeswitch.org'),
    ('Newfies-Dialer', 'http://www.newfies-dialer.org'),
    ('CDR-Stats', 'http://www.cdr-stats.org'),
    ('A2Billing', 'http://www.a2billing.com'),
)

# Social widget
SOCIAL = (
    ('About Me', SITEURL + '/about.html'),
    ('Twitter', 'https://twitter.com/areskib'),
    ('Linkedin', 'http://es.linkedin.com/in/areski'),
    ('Github', 'http://github.com/areski/'),
)

DEFAULT_PAGINATION = 10

MENUITEMS = (
    ('github', 'http://github.com/areski'),
)

FILES_TO_COPY = (
    ('extra/robots.txt', 'robots.txt'),
    ('extra/CNAME', 'CNAME'),
)

DISQUS_SITENAME = "areski-blog"
GOOGLE_ANALYTICS = "UA-325034-3"
GRAVATAR = 'http://www.gravatar.com/avatar/2319bfc31c8757d206a3df6b34d9a852.png'
GITHUB_URL = 'http://github.com/areski/'

# Syte theme specific settings
##############################

# HTML related settings
AUTHOR = u"Areski Belaid"
SITENAME = u"Areski Belaid's blog"
SITESUBTITLE = u"Telefony with a Neurotic Pythonist"
SITE_DESCRIPTION = u'Personal website and blog of Arezqui Belaid.'
ABOUT = SITESUBTITLE
GITHUB_URL = "http://github.com/areski/"
SITE_KEYWORDS = u'python, telefony, freeswitch, asterisk'
WEBASSETS = True

# Links
DISPLAY_HOME_ON_MENU = False
GOOGLE_PLUSONE = True

# Social integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_USERNAME = 'areski'
GPLUS_INTEGRATION_ENABLED = True
GPLUS_USERNAME = '105014012676631081488'
GPLUS_API_ACCESS = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'areskib'
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_USERNAME = 'XXXXXXXXXX'
INSTAGRAM_API_ACCESS = 'XXXXXXXXXXXXXXXXXXX'
CONTACT = u'areski@gmail.com'
