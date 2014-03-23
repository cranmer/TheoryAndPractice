Title: Testing
date: 2014-03-21 10:53
Slug: Testing
Category: Blog
Authors: Kyle Cranmer
Summary: 

I'm Kyle Cranmer, this is my site. [a link]({filename}../HelloWorld.md)

And here is an image [Alt Text]({filename}../images/kyle-andys-party-miras-photo.jpg)

{% img /images/kyle-andys-party-miras-photo.jpg 300 200 Me %}

{% video /images/spyro.mp4 300 200 %}


{% youtube Pv_DtHuj5Ds %}

{% include_code learnEmbedding.py lang:python learnEmbedding %}

Notes on getting notebook to work:
ipython command line worked, but import IPython wasn't working. Was a virtualenv issue, did a pip install (very fast) and all good now. Adding the EXTRA_HEADER doesn't work until the _nb_header.html is generated. If there is no check for the file, the devserver has problems. I wasn't sure where to put the 
{% literal if EXTRA_HEADER %} stuff, but found that it should go in themes/base.html. Unfortunately, the _nb_header isn't playing well with the pelican-bootstrap3 theme... the notebook is styled, but the menu, buttons, and headers of the rest of the page are modified.

 
{% notebook Spirograph3d.ipynb cells[0:9] %}

How do I style the literal line below?

{% literal include_code learnEmbedding.py lang:python learnEmbedding %}

<!--

test notebook

-->