Title: Migrating To Pelican
date: 2014-03-21 10:53
Slug: Testing-Pelican-Migration
Category: Blog
Authors: Kyle Cranmer


So, I'm taking the leap and migrating from Wordpress to 
[pelican](http://getpelican.com). 
Less than year ago [I switched to Wordpress](/2013/06/next-up-flask/) from an ancient Zope site and was 
happy to have something that worked easily.  I was very busy at the time 
and I guess I felt old and didn't want to deal with hacking just to make
a blog post.  However, when I tried to experiment with d3 and wordpress it
was ugly, even though there were some plugins to help.  And when I tried to
include an IPython notebook, all I could do was an <iframe\> embed, and that
was ugly both visually and technically.

Recently, I've been playing more with IPython and had more familiarity with 
the git-o-sphere.  I'd like to blog more with code and technical stuff, and I was taken
with the seamlessness of [Jake  Vanderplas's Pythonic Perambulations](http://jakevdp.github.io). 
I also like the nice mix of static html and dynamic widgets and services, 
so I decided to give it a go.  Currently, the site is being published to GitHub 
pages at `cranmer.github.io`, but I'm going switch it over to `theoryandpractice.org` 
soon.  I'm still conflicted if I should use GitHub's hosting or my current hosting 
service since I'm paying for a [flask server](http://flask.theoryandpractice.org) 
and I don't plan on giving that up.

Anyways, I'll say I drew heavily on these resources:

- [Jake  Vanderplas's migration](http://jakevdp.github.io/blog/2013/05/07/migrating-from-octopress-to-pelican/) including various liquid plugins
- [arunrocks migration](http://arunrocks.com/moving-blogs-to-pelican/) and  [This site](http://martinbrochhaus.com/pelican2.html)
- [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) using simplex from [Bootswatch](http://bootswatch.com)
- Conversations with [Sven Kreiss](http://www.svenkreiss.com) and [Forman-Mackey](http://dan.iel.fm)

Great! Now I can render\_math like $e^{i\pi}+1 = 0$ and include a little block of python with pygments

```python
    def main():
        print 'welcome to Pelican'
```

I was able to export my wordpress site to XML and import using the pelican-import tool.  The images were a bit of a disaster, so I had to manually change all of that. I was also able to make the URLs to my posts to keep the old wordpress convention. I haven't yet moved the site to `theoryandpractice.org`, but this will keep the links working if/when I do.  

###Workflow issues:

I'm happy to use `virtualenv`, but it's not quite clear to me the best way to use it for pelican development. Should I be using `virtualenv` for my pelican installation, which I then use to build my site (which I think of as some data); or am I using `virtualenv` to encapsulate all my site's dependencies (themes, plugins, etc.) ? Currently, I'm not using git submodules, b/c I've heard they are somewhat `evil` (TM). This also affects the use of `ghp-import`... am I using the same repository for my pelican content and configuration as I use to deploy?  Currently, I have a separate repository for pelican source and the rendered html.


###Issues:

- How do I style the liquid literal {% literal include_code learnEmbedding.py lang:python learnEmbedding %}
- {% literal youtube %} tag working, but
    - does it work with start/end time?
    - does it support change to height/width of iframe?

###Notes on getting notebook to work

- IPython command line worked, but import IPython wasn't working. Was a virtualenv issue, did a pip install (very fast) and all good now. 
- Adding the EXTRA_HEADER doesn't work until the _nb_header.html is generated. If there is no check for the file, the devserver has problems. 
- I wasn't sure where to put the {% literal if EXTRA_HEADER %} code, but found that it should go in themes/base.html. Unfortunately, the _nb_header isn't playing well with the pelican-bootstrap3 theme... the notebook is styled, but the menu, buttons, and headers of the rest of the page are modified.
- ok, made _nb_header_minimal only taking the last ~113 lines of _nb_header that have the script to call mathjax on the notebook (else the math doesn't render for the imported notebook) and the highlight style. That gives me the basics to make the notebook look reasonable.
- another idea to [wrap notebook](https://twitter.com/minrk/status/448164391242829824)

Notes on themes:

- see note above about where to stick the EXTRA_HEADER for the IPython notebok.
- using Bootstrap3 to get the twitter  and recent publication feeds to have a nice responsive layout on homepage

###Some fun

Ok, enough talk. Let's try a few cells from my IPython notebook of a [Spirograph Animation](http://nbviewer.ipython.org/url/cranmer.github.io/downloads/notebooks/Spirograph3d.ipynb?create=1) for fun.  I'll type:

{% literal notebook downloads/notebooks/Spirograph3d.ipynb cells[9:10] %}

and that produces:
 

{% notebook downloads/notebooks/Spirograph3d.ipynb cells[9:10] %}

So far so good, now let's try to embed the end of the notebook that has the animation with 
{% literal notebook downloads/notebooks/Spirograph3d.ipynb cells[9:10] %}

{% literal notebook downloads/notebooks/Spirograph3d.ipynb cells[14:15] %}

{% notebook downloads/notebooks/Spirograph3d.ipynb cells[14:15] %}

Animation looks good, but doesn't seem to work on my phone. 

_Many thanks to my lovely wife Danielle for putting up with me this weekend while my daughter refused to nap!_


<!--

test notebook

-->