Title:  Hello 2016!
date: 2016-01-10
Slug: Hello 2016!
Category: Blog
Status: draft
Tags:  physics, machine learning, statistics
Authors: Kyle Cranmer

Well, it's been a while since I wrote anything on this blog -- a pretty
good sign that I've been busy. 2015 was a fantastic year for me.
I can't say enough good things about my sabbatical at UC-Irvine.
In addition to perfect weather, close friends, and hoppy beer, I also found time to think
about new things that lay the groundwork for new research programs.
I say 'programs', because I don't mean isolated projects, but a 
large body of interrelated research.

Most of these new ideas are a mix of statistical and machine learning
methodology applied to problems that come up in high-energy physics (HEP).
For years, I've thought that many of the problems that we encounter in 
HEP much be much more general, but I've had a hard time 
succinctly characterizing the common theme. 
I used to focus on three major ingredients:

   * large, distributed collaborations

   * complicated sensor environment

   * scientifically motivated data modeling


These are all trends, I would say. 'Big Data' and 'Data Science' are implicit to them all. 
The 'large, distributed collaborations' theme is easily 
associated to the buzz word 'Big Science', which is exemplified by the LHC experiments.
Large collaborations are becoming more common in other areas, like genomics and even 
[math](http://polymathprojects.org).  The 'complicate sensor environment' theme 
is a more specific way of referring to 'Big Data' that brackets 
complicated experiments like the LHC and the 'Internet of Things'.

The odd man out in this thematic triumvirate is `scientifically motivated data modeling'.
By this I mean traditional scientific theory, but what is the corresponding buzz word?
I don't care about buzz words, but if I'm trying to make the case that these ideas
I'm thinking about are more general and the work going on at the LHC really represents
"a harbinger for things to come", then I should be able to identify a corresponding buzzword. 

The best I could do early on were the following. One is the buzzword 'Big Model'.
The main point here is that if you want to get the most out of 'Big Data', then
you need a Big Model. Often the Big Model referred to some black-box machine learning
algorithm, and the 'Big' was an imprecise way of saying the model had large 
learning capacity.  I appreciated that point, but in the context of my work I would
think of the big statistical models that we build at the LHC using 
[RooFit/RooStats](http://localhost:8000/2014/03/roofit-statistical-modeling-language-in-ipython-notebook/) tools. 
The other buzzword-laden body of work that assured me that the theme is 
more general than HEP is the "[4th paradigm](http://research.microsoft.com/en-us/collaboration/fourthparadigm/)".
This appreciates that the scientific situation is really different, but doesn't eschew 
appreciation for traditional scientific theories. 

But during my sabbatical I started to focus on the term 'Likelihood-Free' as a way of referring
to inference when the theory that predicts the data is encoded in a computer simulation.
The important part about the likelihood-free setting is that one can perform simulations 
and generate simulated data, but given some data one cannot evaluate the likelihood for the
parameters of the simulation. 


I recently [Reinventing Discovery](http://press.princeton.edu/titles/9517.html)


   the fact that we are really 
interested in 


Note, added a little to `pelican-bootstrap3/templates/includes/liquid_tags_nb_header.html`

<!--

{% thebe really-interactive-posts.ipynb %}

{% notebook NetworkxD3example.ipynb %}

<iframe width="400" height="400" src="http://127.0.0.1:8000/Net.html" frameborder="0"  allowfullscreen ></iframe>
-->
