AUTHOR = 'Benoît GRISOT'
SITENAME = 'Coubiac'
SITEURL = ''
STATIC_PATHS = ['images']

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

GITHUB_URL = 'http://github.com/Coubiac/'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'
RSS_FEED_SUMMARY_ONLY = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
LINKS = (('Calcul VLSM', 'https://vlsm.triscel.ovh'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/benoitgrisot'),
          ('github', 'https://github.com/Coubiac'),
          ('twitter', 'https://twitter.com/benoit_grisot'),
          )

THEME = 'pelican-themes/pelican-dark-theme-master'
# SIDEBAR_DIGEST = 'un sysadmin'
# # FAVICON = 'url-to-favicon'
# DISPLAY_PAGES_ON_MENU = True
# TWITTER_USERNAME = 'benoit_grisot'
# MENUITEMS = (('Blog', SITEURL),)
# DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
AUTHOR_EMAIL = 'benoit.grisot@gmail.com'
AUTHOR_AVATAR = '/images/static/Gravatar.jpg'
AUTHOR_MENU_BACKGROUD = '/images/static/menu.jpg'