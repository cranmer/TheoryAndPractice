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

#DISPLAY_PAGES_ON_MENU =False
#MENUITEMS = (('Projects','/pages/projects.html'),)

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
		  ('Quantum Diaries', 'http://www.quantumdiaries.org/'),
		  ('Me @ Quantum Diaries','http://www.quantumdiaries.org/author/kyle-cranmer/'),
		  ('Not Even Wrong','http://www.math.columbia.edu/~woit/wordpress/'),
		  ('Cocktail Party Physics','http://twistedphysics.typepad.com/cocktail_party_physics/'),
		  ('Résonaances','http://resonaances.blogspot.com/'),
		  ('Matt Strassler','http://profmattstrassler.com/'),
		  ('Life as a physicist','http://gordonwatts.wordpress.com/'),
		  ('Tommaso Dorigo','http://www.science20.com/physics'),
		  ('Cosmic Variance','http://blogs.discovermagazine.com/cosmicvariance/'),
		  ('Collider Blog','http://muon.wordpress.com/'),
		  ('Symmetry Breaking','http://www.symmetrymagazine.org/breaking'),
		  ('INSPIRE','http://blog.inspirehep.net/'),
		  ('Data Pub','http://datapub.cdlib.org/'),
		  ('Hogg’s Research','http://hoggresearch.blogspot.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/kylecranmer'),
          ('github', 'http://github.com/cranmer'),
          ('linkedin','http://www.linkedin.com/in/kylecranmer'),
          ('google+','https://plus.google.com/106689822196584540592/posts'),
          ('flickr','http://www.flickr.com/photos/hoonynoo/'),)

CC_LICENSE="CC-BY"

DEFAULT_PAGINATION = False

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
THEME = 'notmyidea'
PYGMENTS_STYLE='default'
#PYGMENTS_STYLE='friendly'
#THEME = '../pelican-bootstrap3'
#THEME = '/Users/cranmer/virtualenvs/pelican/lib/python2.7/site-packages/pelican/themes/pelican-bootstrap3'
# This requires Pelican 3.3+





#INDEX_SAVE_AS = 'index.html'

#the deault _nb_header is changing 
#fonts etc. of rest of notmyidea and pelican-bootstrap3 themes
#looks ok in notmyidea, but no style at all in bootstrap3
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')
#EXTRA_HEADER = '' #need to flush

