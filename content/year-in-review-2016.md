Title: Year in Review: 2016
date: 2016-12-30
Slug: year-in-review-2016
Category: Blog
Tags: Machine Learning, Higgs, Open Science, Physics
Authors: Kyle Cranmer
JavaScripts: d3.min.js, packages.js, collaboration-map.js, test-collaboration-map.js
Stylesheets: concept-map.css, concept-map-padding.css

### Progress
<div class="progress">
  <div class="progress-bar progress-bar-danger" style="width: 10%"></div>
</div>

Despite the reputation of 2016 as a terrible year, it was pretty good for me on a personal and professional level.
Many of the ideas that were born during my [sabbaticall]({filename}/Sabbatical.md) matured this year. Many of my [collaborations]({filename}/collaboration-map.md) also flourished.

### The 750 GeV Excess

The year started with a bang with a bumplet in the LHC data -- specifically the [750 GeV diphoton excess](https://en.wikipedia.org/wiki/750_GeV_diphoton_excess). This led to lots of excitement in the field and in the [media](http://www.nytimes.com/2015/12/16/science/physicists-in-europe-find-tantalizing-hints-of-a-mysterious-new-particle.html?_r=1). I was interviewed by the [New York Times]((http://www.nytimes.com/2015/12/16/science/physicists-in-europe-find-tantalizing-hints-of-a-mysterious-new-particle.html?_r=1), [Vox](http://www.vox.com/2016/9/21/12691576/lhc-cern-new-subatomic-particle), and NPR's Here and Now about it.

<iframe width="100%" height="124" scrolling="no" frameborder="no" src="//embed.wbur.org/player/hereandnow/2015/12/16/cern-fundamental-particle-nature"></iframe>

One of the concerns in interpreting the significance of that bump in the data was that we perform so many different tests
of the Standard Model that we expect to see big fluctuations occasionally. We often call this the look-elsewhere effect.
Conventional wisdom is that this effect goes away because we have two experiments seeing the same thing. While it's true that having two experiments reduces this effect, it doesn't go away entirely. I was thinking about all of this early in the year and came up with a nice way to [connect Gaussian Processes and the look-elsewhere effect ](http://nbviewer.jupyter.org/github/cranmer/look-elsewhere-2d/blob/master/two-experiment-lee-testing.ipynb).

The excitement around the bump was extraordinary, there were more than 100 papers on the subject by February. 
In March there was a lot of introspection in the field about this phenomena. I decided to write an [April Fools Day]({filename}/Supersplit.md) paper about it. It's full of subtle physics and statistics references -- so while it's not at all accessible, I'm pretty happy with it.

Unfortunately, the 750 GeV diphoton bump disappeared with more data. André David kept track of the number of citations 
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/Run2Seminar?src=hash">#Run2Seminar</a> 1st (only?) anniversary.<br>3 clear <a href="https://twitter.com/hashtag/750GeV?src=hash">#750GeV</a> <a href="https://twitter.com/hashtag/diphoton?src=hash">#diphoton</a> phases:<br>- Inflationary Xmas.<br>- Moriond steady state.<br>- Post-ICHEP flatline. <a href="https://t.co/7UUQTrTo5P">pic.twitter.com/7UUQTrTo5P</a></p>&mdash; André David (@DrAndreDavid) <a href="https://twitter.com/DrAndreDavid/status/809410781242683392">December 15, 2016</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


### Carl and likelihood-free inference

One of the most significant outcomes of my sabbatical at UC-Irvine was this idea that we can use classifiers from machine learning to approximate an intractable likelihood function and perform inference. 
While the term is unfamiliar, intractable likelihoods is one of the defining challenges of data analysis for experimental high-energy physics. Our field has developed a lot of strategies, but we have not formulated them 
in this way. I've found that formulating them this way really helps clarify many issues and makes it 
clear that there are ample opportunities for improvement. Moreover, many other scientific disciplines can
be formulated in this way, which facilitates communication between the scientific domain and the statistics 
/ machine learning communities.

In 2015, I started to focus on this topic of likelihood-free inference and wrote my first [non-physics paper](https://arxiv.org/abs/1506.02169v1). 
The idea was there, but it needed to be rewritten and supported by examples.
In late 2015, I hired Gilles Louppe, who has a PhD in Computer Science and focuses on machine learning. 
He started working on [Carl](http://diana-hep.org/carl/), a toolbox for likelihood-free inference that 
implemented the techniques in the paper. I'd already been working with Juan Pavez on examples, and I 
invited Gilles and Juan as authors for [version 2](https://arxiv.org/abs/1506.02169) of the paper.


**February & March** 

*  CARL

### Carl and likelihood-free inference

**April**
  * April Fools
  * HEPAP
  * Yale


## May

 * JHU
 * INSPIRE
 * Last Days of Classes 

## June

  * TASI & Information Geometry for Higgs EFT
  * ATLAS Week


## July

  * PFC

## August

  * ASPEN

  * DASPOS, CAP, yadage

## September

  * DASPOS, CAP, yadage

  * CDS Masters : Physics track

## October

  * MSDSE Summit

## November

  * PFC news

  * Rubik's Cube

## December

  * Jet Paper
  * MIT
  * NIPS 
    * Keynote
    * Bijections!
    * Probabilistic Programming
  * Information Geometry paper
  * DIANA summary
  * CDS Masters : first projects
  * [Collaboration Map](/collaboration-map/)


  <img src="/images/year-in-review-GH-2016.png" alt="GitHub Activity in 2016" width="90%" />

  <iframe src="https://docs.google.com/presentation/d/1So1U6v-e6Ai88gXw1Toy-9OzYNnGwCrCnYMngLeB1l8/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

