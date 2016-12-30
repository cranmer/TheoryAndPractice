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

The year started with a bang with a bumplet in the LHC data -- specifically the [750 GeV diphoton excess](https://en.wikipedia.org/wiki/750_GeV_diphoton_excess). This led to lots of excitement in the field and in the [media](http://www.nytimes.com/2015/12/16/science/physicists-in-europe-find-tantalizing-hints-of-a-mysterious-new-particle.html?_r=1). I was interviewed by the [New York Times](http://www.nytimes.com/2015/12/16/science/physicists-in-europe-find-tantalizing-hints-of-a-mysterious-new-particle.html?_r=1), [Vox](http://www.vox.com/2016/9/21/12691576/lhc-cern-new-subatomic-particle), and NPR's Here and Now about it.

<div align="center">
<iframe width="80%" align="center" height="124" scrolling="no" frameborder="no" src="//embed.wbur.org/player/hereandnow/2015/12/16/cern-fundamental-particle-nature"></iframe>
</div><br />

One of the concerns in interpreting the significance of that bump in the data was that we perform so many different tests
of the Standard Model that we expect to see big fluctuations occasionally. We often call this the look-elsewhere effect.
Conventional wisdom is that this effect goes away because we have two experiments seeing the same thing. While it's true that having two experiments reduces this effect, it doesn't go away entirely. I was thinking about all of this early in the year and came up with a nice way to [connect Gaussian Processes and the look-elsewhere effect ](http://nbviewer.jupyter.org/github/cranmer/look-elsewhere-2d/blob/master/two-experiment-lee-testing.ipynb).

The excitement around the bump was extraordinary, there were more than 100 papers on the subject by **February**. 
In **March** there was a lot of introspection in the field about this phenomena. I decided to write an [**April** Fools Day]({filename}/Supersplit.md) paper about it. It's full of subtle physics and statistics references -- so while it's not at all accessible, I'm pretty happy with it.

Unfortunately, by **August** the 750 GeV diphoton bump had disappeared with more data. André David kept track of the number of citations throughout the year.

<div align="center">
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/Run2Seminar?src=hash">#Run2Seminar</a> 1st (only?) anniversary.<br>3 clear <a href="https://twitter.com/hashtag/750GeV?src=hash">#750GeV</a> <a href="https://twitter.com/hashtag/diphoton?src=hash">#diphoton</a> phases:<br>- Inflationary Xmas.<br>- Moriond steady state.<br>- Post-ICHEP flatline. <a href="https://t.co/7UUQTrTo5P">pic.twitter.com/7UUQTrTo5P</a></p>&mdash; André David (@DrAndreDavid) <a href="https://twitter.com/DrAndreDavid/status/809410781242683392">December 15, 2016</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</div><br />

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
That was our main focus in **February** and **March**.
In the process the core idea really matured and we made connections to many different topics, 
including generative models, importance sampling / reweighting, and adversarial training. 
These all ended up being themes of my talk at NIPS in **December**.

<div align="center">
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">This set of connections has fascinated me for the last year. So many different ideas come together under one umbrella. <a href="https://t.co/eeiVP32ASo">https://t.co/eeiVP32ASo</a></p>&mdash; Kyle Cranmer (@KyleCranmer) <a href="https://twitter.com/KyleCranmer/status/814088701403873280">December 28, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</div><br />


### Major progress on long-term projects

This year also saw progress on a number of long-term projects. 

#### Recast & Analysis Preservation

Back in 2009, Itay Yavin, James Beacham, and I went back to old ALEPH data
and looked for the Higgs there before it was discovered at the LHC.
There was a nice [Wired](https://www.wired.com/2015/01/higgs-discovery-hijack-attempt/)
article about that story. It also initiated my interest in data and software preservation,
open science, reproducibility, etc. In particular, in 2010 Itay Yavin and I proposed 
[Recast](https://arxiv.org/abs/1010.2506) -- a system for reinterpreting the results of 
searches for new particles. In early 2012 we launched a [beta version](http://recast.perimeterinstitute.ca/)
of the Recast front-end website. Of course, the Higgs was found months later and that
distracted all work on Recast for a few years. In 2015, my student Lukas Heinrich picked it up,
and started to work on the back end that does all the heavy lifting. The ATLAS collaboration 
also formed a small task force to look into issues around analysis preservation and reinterpretation,
which I served on. Simultaneously, the group that produced CERN's Open Data Portal started putting
more emphasis into the CERN Analysis Preservation project. We've been working with them since the 
beginning and now the entire effort is making great progress. Along the way, we realized that
*yadage*, the tool Lukas developed for the Recast backend, provides a generic, flexible system for distributed workflows, where each processing step can be containerized (eg. with docker) independently. 

When LIGO announced their discovery of gravitational waves in **February**, they took an important
step in releasing the data and code related to the discovery. Lukas and I quickly dockerized the
environment needed for their Jupyter notebook and made [ligo-binder](https://github.com/cranmer/ligo-binder), 
which you can run in your browser with no installation.

All of this work on reproducible workflows ties in nicely with likelihood-free inference, because
in likelihood-free inference, you need to encapsulate the simulation pipeline. 
I wrote a bit about this earlier after our [Reproducibility Symposium at NYU]({filename}/reproducibility-symposium.md) in **May**.

A huge boost to the project came in *September* when we found out that the NSF approved an extension
to the [DASPOS](http://daspos.org/) project to further the development of Recast and deploy 
the *yadage* workflow execution engine as part of the CERN Analysis Preservation project.
With this funding, we are working with Heiko Müller (a research engineer as part of the MSDSE / NYU CDS) 
and Tim Head (previously on LHCb).

#### HEPAP 

In **April** I went to Washington DC and was sworn in as a special government employee to be
a member of the High Energy Physics Advisory Panel (HEPAP), which has advised the Federal Government 
on the national program in experimental and theoretical high energy physics research since 1967. 
We discussed the planning and progress in the field since [the P5 Report](http://www.usparticlephysics.org/).

#### INSPIRE & HEPData

This was also a big year from [INSPIRE](http://inspirehep.net) and [HEPData](http://hepdata.net), 
two important parts of the cyberinfrastructure for 
high energy physics. I am on the advisory board for both of these projects and work with them quite closely.
I was part of the discussion that led to the decision to migrate the legacy version of HEPData to the
Invenio platform that powers INSPIRE, the CERN Open Data Portal, Zenodo, and other sites. Lukas and
I worked with Eamonn Maguire and others in the HEPData team as part of this migration. It was 
a real pleasure to work with Eamonn, who makes awesome products and has a great design sense. 
The [new HEPData](https://indico.cern.ch/event/512652/timetable/) was announced in **April** and 
Lukas [presented it at CHEP](https://indico.cern.ch/event/505613/contributions/2227685/) in **October**.

In **May** we had an I went to SLAC for the INSPIRE advisory board meeting. INSPIRE has
also been migrating to a new version of INVENIO and the site will be *much* nicer. 
There is a preview of the site at [qa.inspirehep.net](https://qa.inspirehep.net/). 
During that meeting, I also presented some vision for how INSPIRE fits into the 
cyberinfrastructure priorities at the NSF and various foundations. I've also initiated
some discussions with the NYU library about getting more directly involved. 

### ATLAS Week

Despite warnings from some close friends, I put in a proposal to host ATLAS week at NYU. 
We won the bid and that started the incredibly time consuming process of planning the meeting.
Luckily, I had a lot of help from Connie Potter, Petya Lilova, Jennifer Morral, Andy Haas, Allen Mincer,
and Ben Kaplan in organizing it. Organizing ATLAS week consumed essentially all of **June** and probably another
month integrated over the year. Luckily, it went quite well. We had more than 300 people for the first ATLAS week
hosted in the US in more than a decade. 

<div align="center">
<img src="/images/atlas-week-group-IMG_7192.JPG" alt="ATLAS Week photo" width="70%" align="center" />
</div><br />

### Physics Track in the Masters of Data Science

The [Master's in Data Science at NYU's Center for Data Science](http://cds.nyu.edu/academics/ms-in-data-science/) has been very successful, 
with more than a thousand applications less than 100 spots. As part of the Moore-Sloan Data Science Environment at
NYU, I spend quite a bit of time thinking about how we can develop a sustainable resource of data science in academia,
which can focus on scientific problems. In **April** I had the idea of creating some sort of hybrid masters
program between data science and physics. I proposed the idea and got a lot of encouragement to develop it further.
The physics department gave leave from teaching in the fall to make it into a reality. We ended up creating a 
*physics track* in the existing Masters of Data Science with special curriculum requirements. In addition to the 
core data science courses, the students that enter this track will take two physics courses and spend two semesters
doing research on physics-related topics. Faculty in the physics department have so many ideas for data science projects 
relevant to physics research, but typically these projects are either seen as a distraction for a typical PhD student,
or the physics students don't really have the right skill set. In addition to being increasing the research capacity
of the physics department, this program will help differentiate the graduates. Physicists are highly sought after
in data science roles, so perhaps the students that go through this track will have a competitive advantage. 
The Physics Department, the Faculty of Arts and Science, and the Center for Data Science approved the track in *September*. The program will start in the fall of 2017 and we are [taking applications now](http://cds.nyu.edu/academics/ms-in-data-science/).

As a soft-launch for the Physics Track in the MS in Data Science, I proposed a few Capstone projects to the current masters students. Since the students don't have any particular physics background, it was also good practice for
posing problems and preparing data in a way that does not require a lot of domain expertise. I was surprised that five groups picked my physics projects. So while I wasn't teaching in the fall, I was advising 15 masters students! I was impressed with the progress they made in one semester. The tweet below starts a thread that gives a short description of those five projects. 

<div align="center">
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">This semester I advised 5 physics-related Capstone projects for <a href="https://twitter.com/NYUDataScience">@NYUDataScience</a> Masters Program.  <a href="https://t.co/IwpFfVwYlx">https://t.co/IwpFfVwYlx</a> (1/n) <a href="https://t.co/9FTnuALBoa">pic.twitter.com/9FTnuALBoa</a></p>&mdash; Kyle Cranmer (@KyleCranmer) <a href="https://twitter.com/KyleCranmer/status/809843960965435393">December 16, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</div><br />


### Higgs Effective Field Theory


### NIPS

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Here are the slides from my talk at <a href="https://twitter.com/hashtag/NIPS2016?src=hash">#NIPS2016</a> on machine learning &amp; likelihood-free inference for particle physics<a href="https://t.co/pvmPCFexyZ">https://t.co/pvmPCFexyZ</a> <a href="https://t.co/72EDdwVnXE">pic.twitter.com/72EDdwVnXE</a></p>&mdash; Kyle Cranmer (@KyleCranmer) <a href="https://twitter.com/KyleCranmer/status/806537845909422080">December 7, 2016</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

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

