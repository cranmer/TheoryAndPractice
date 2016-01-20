Title:  Decomposing Classification For Mixture Models
date: 2015-06-12
Slug: Decomposed Classifier
Category: Blog
Tags:  physics, machine learning, statistics
Authors: Kyle Cranmer

So I recently [learned](https://twitter.com/KyleCranmer/status/604338535282311168) about the ability to convert IPython notebooks into slides using nbconvert.
Not sure how I overlooked that capability of nbconvert. There are some (somewhat out of date) references
on [Damián Avila's blog](http://www.damian.oquanta.info/posts/make-your-slides-with-ipython.html).

I'm pretty excited about the idea of using IPython notebooks as a more effective way of 
communicating results within the LHC collaborations. 
As part of the [DIANA/HEP](http://diana-hep.org) project, I'm trying to promote these kinds of collaborative tools
that improve reproducibility and streamline (internal or external) sharing.
There are some obstacles because most of
the [200,000 presentations / year](https://indico.cern.ch/category/0/statistics) at the LHC are internal documents not meant for public consumption. This means either integrating nbconvert directly into [indico](https://indico.cern.ch) 
or providing a similar service as nbviewer that can deal with CERN authentication and credentials.


Anyways, since I'm learning about this, I thought I'd try it out by writing a few slides
related to Section 5.4 of my recent paper 
*Approximating Likelihood Ratios with Calibrated Discriminative Classifiers*, [http://arxiv.org/abs/1506.02169](http://arxiv.org/abs/1506.02169). The slides are just a demonstration of some basic algebra, but 
I've recently started working with [Juan Pavez](https://twitter.com/juanpavez) on demonstraiting this technique with real classifiers (scikit-learn, theano, TMVA, ...). Hopefully more to come on this topic.

I've embed the slides below, or if you are on your phone you can try this [direct link to the slides](/downloads/notebooks/DecomposingTestsOfMixtureModels.slides.html#) since I'm not sure how to do a responsive embed.
Click on the slides once and then you can use your $\leftarrow$ $\uparrow$ $\rightarrow$  $\downarrow$ keys to navigate (or click the navigation in the bottom right of the slides).

<div class="row">
  <div class="col-md-6">
<iframe src='/downloads/notebooks/DecomposingTestsOfMixtureModels.slides.html#/' width="800" height="600"></iframe>
</div>
</div>

