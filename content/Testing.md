Title: Testing Pelican Migration
date: 2014-03-21 10:53
Slug: Testing-Pelican-Migration
Category: Blog
Authors: Kyle Cranmer

Testing:

- Here is [a link]({filename}../inspired-by-the-higgs-a-step-forward-in-open-access.md) to a local file
- liquid {% literal img %} tag working    
- {% literal youtube %} tag working, but
    - does it work with start/end time?
    - does it support change to height/width of iframe?
- render\_math works: $e^{i\pi}+1 = 0$
- simple inline `code` markup
- a little block of python with pygments

```python
    def main():
        print 'welcome to Pelican'
```

Notes on getting notebook to work

- ipython command line worked, but import IPython wasn't working. Was a virtualenv issue, did a pip install (very fast) and all good now. 
- Adding the EXTRA_HEADER doesn't work until the _nb_header.html is generated. If there is no check for the file, the devserver has problems. 
- I wasn't sure where to put the {% literal if EXTRA_HEADER %} code, but found that it should go in themes/base.html. Unfortunately, the _nb_header isn't playing well with the pelican-bootstrap3 theme... the notebook is styled, but the menu, buttons, and headers of the rest of the page are modified.


{% literal notebook Spirograph3d.ipynb cells[1:9] %}
 
 - - -

{% notebook Spirograph3d.ipynb cells[1:9] %}

How do I style the literal line below?

{% literal include_code learnEmbedding.py lang:python learnEmbedding %}

<!--

test notebook

-->