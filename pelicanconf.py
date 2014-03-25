#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kyle Cranmer'
SITENAME = u'Theory And Practice'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU =False
MENUITEMS = (
#			('About','/index.html'),
			('Research','/pages/Research.html'),
			('Projects','/pages/projects.html'),
			('Media & Outreach','/pages/in-the-news.html'),)

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
		  ('Quantum Diaries', 'http://www.quantumdiaries.org/'),
#		  #('Me @ Quantum Diaries','http://www.quantumdiaries.org/author/kyle-cranmer/'),
		  ('Not Even Wrong','http://www.math.columbia.edu/~woit/wordpress/'),
		  ('Cocktail Party Physics','http://twistedphysics.typepad.com/cocktail_party_physics/'),
		  ('Résonaances','http://resonaances.blogspot.com/'),
		  ('Matt Strassler','http://profmattstrassler.com/'),
#		  #('Life as a physicist','http://gordonwatts.wordpress.com/'),
		  ('Tommaso Dorigo','http://www.science20.com/physics'),
#		  #('Cosmic Variance','http://blogs.discovermagazine.com/cosmicvariance/'),
#		  #('Collider Blog','http://muon.wordpress.com/'),
		  ('Symmetry Breaking','http://www.symmetrymagazine.org/breaking'),
		  ('INSPIRE','http://blog.inspirehep.net/'),
		  ('Data Pub','http://datapub.cdlib.org/'),
		  ('Hogg’s Research','http://hoggresearch.blogspot.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/kylecranmer'),
          ('github', 'http://github.com/cranmer'),
          ('linkedin','http://www.linkedin.com/in/kylecranmer'),
          ('google+','https://plus.google.com/106689822196584540592/posts'),
          ('youtube','http://youtube.com/user/cranmer'),
          ('flickr','http://www.flickr.com/photos/hoonynoo/'),
          ('figshare','http://figshare.com/authors/Kyle%20Cranmer/432748'),
          ('ImactStory','http://impactstory.org/KyleCranmer'))

CC_LICENSE="CC-BY"

DEFAULT_PAGINATION = 6

#use URLs that match old wordpress site
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

####################################################
# Additions 
STATIC_PATHS = ['images', 'downloads', 'downloads/notebooks' 'favicon.png']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

PLUGIN_PATH = '../pelican-plugins/'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
			'liquid_tags.youtube', 'render_math',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

THEME = 'pelican-bootstrap3'
#THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'
#THEME = '../pelican-bootstrap3'
#THEME = '/Users/cranmer/virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3'
# This requires Pelican 3.3+

#For pelican-ootstrap3
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_THEME='yeti'
BOOTSTRAP_THEME='superhero' #nice but, background doesn't work well with code as is
BOOTSTRAP_THEME='cosmo'
DISPLAY_BREADCRUMBS=False
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
#ABOUT_ME="I'm a professor at NYU interested in particle physics, open science, data science, and science communication to the broader public."
#AVATAR='/images/kyle-andys-party-miras-photo.jpg'
AVATAR=None
ABOUT_ME=None
#TWITTER_WIDGET_ID='353505377641447424'
TWITTER_WIDGET_ID=''
#GITHUB_USER='cranmer'
#GITHUB_REPO_COUNT=True
#GITHUB_SKIP_FORK=True
#GITHUB_SHOW_USER_LINK=True




#INDEX_SAVE_AS = 'index.html'

#the deault _nb_header is changing 
#fonts etc. of rest of notmyidea and pelican-bootstrap3 themes
#looks ok in notmyidea, but no style at all in bootstrap3
EXTRA_HEADER = open('_nb_header_minimal.html').read().decode('utf-8')
#EXTRA_HEADER = '' #need to flush

