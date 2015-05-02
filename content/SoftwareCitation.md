Title: Software: citation and status
date: 2015-5-01 13:53
Slug: Software: citation and status
Category: Blog
Tags:  physics, open science
Authors: Kyle Cranmer

I'm just finishing an intense and exciting week focusing a lot on the role of software and data in science.
The big event was a workshop on [Indexing Astronomical Software](https://github.com/astronomy-software-index/2015-workshop/blob/master/README.md#agenda) jointly organized by AAS and GitHub and supported by the Alfred P. Sloan Foundation. It was a small workshop with about twenty people that are deeply involved in these issues. I was happy to be invited since I'm not an astronomer, but I think about the issue for particle physics. 

So why was I there? There are a few connections:

   * [Alberto Accomazzi](https://www.cfa.harvard.edu/~alberto/), the Program Manager for the [ADS](http://adswww.harvard.edu) Digital Library, and I are both on the [INSPIRE Advisory Board](http://inspirehep.net/info/general/project/management). 

   * I have good connections with Arfon Smith of GitHub and Lars Holm Nielsen of [Zenodo](http://zenodo.org)/CERN that worked together to create the GitHub [Guide to Make Your Code Citable](https://guides.github.com/activities/citable-code/). Some code of mine was used in the first GitHub → Zenodo DOI example <a href="http://dx.doi.org/10.5281/zenodo.8475"><img src="https://zenodo.org/badge/doi/10.5281/zenodo.8475.svg" alt="10.5281/zenodo.8475"></a>. In just a year there are [nearly 3000](https://zenodo.org/search?cc=software&jrec=11) repositories that now have [DOIs](http://en.wikipedia.org/wiki/Digital_object_identifier).

   * As part of the Moore-Sloan Data Science Environment, I am co-lead for NYU's Open Science and Reproducibility working group 

Shortly before the meeting there was a blog post by Titus Brown asking ["is software a primary product of science?"](http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1983939707). Surprisingly, to many people at least, Titus concluded 'no' it isn't. That led to some discussion on twitter and prompted Dan Katz to write a [response](https://danielskatzblog.wordpress.com/2015/04/22/software-can-be-a-primary-product-of-scientific-research/) on his blog. The discussion is interesting exploring the analogy with instrumentation, the role of software in communication and incapsulation of knowledge. The discussion also got into the very tough set of issues around jobs in academia, the brain drain, and recognition for the essential role of software in science today. I took some time to try to reconcile the situation for myself and wrote some [comments](http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1983939707) in Disqus. Luckily it remained civil and later Titus followed up with [these thoughts](
http://ivory.idyll.org/blog/2015-more-on-software.html#disqus_thread). If you are interested in those topics, I definitely recommend reading some of those links.

So on Sunday I made it to San Francisco. I had an awesome lunch with the team from [experiment.com](http://experiment.com), a crowd funding platform for science, and some artisinal hipster ice cream with my bud Roy Keys (physicist turned data scientist). Monday the AAS/GitHub workshop started with a round of short introductions. That initial stage was fairly efficient because we had all been asked to do some homework before hand. In particular, we were asked to provide a mission statement for the meeting and  to identify the three biggest tangible obstacles that
we saw to achieving the goal as described in our mission statement. Reading these ahead of time was very informative and established some context.  

Later we broke into groups. I was in the "infrastructure & frictions" group. We threw out a lot of issues, Lars helped us organize them, and then [Robert Hanisch](http://www.nist.gov/mml/odi/robert-hanisch.cfm) of NIST helped us reduce the scope a little to something more acheivable for a short time. During lunch we started to have a plan for some specific infrastructure that could help streamline the current curation effort being performed by the [Astrophysics Source Code Library ASCL](http://ascl.net). As for myself, I saw a lot of parallels between ASCL/ADS in astrophysics and HepData/INSPIRE in particle physics. Both ASCL and HepData peform an important curation role, and both are running on a very light budget and there are worries regarding sustainability and older underlying technology. Another obvious parallel
is related to the custom identifiers used by ASCL and [HepData](http://hepdata.cedar.ac.uk), which would ideally be DOIs.
I was volunteered to present for our group when we came back together  -- I think partially because I was an outsider.

After an [exhausting, but productive, session](https://twitter.com/KyleCranmer/status/592832001499131905) we took advantage of GitHub's nicely stocked bar. 


<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">Hanging with <a href="https://twitter.com/arfon">@arfon</a> at <a href="https://twitter.com/github">@github</a> bar <a href="http://t.co/GrAkRgTJjf">pic.twitter.com/GrAkRgTJjf</a></p>&mdash; Kyle Cranmer (@KyleCranmer) <a href="https://twitter.com/KyleCranmer/status/592855685458702337">April 28, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


After a few drinks we had a quick demo session. There was an impressive demo of the [new ADS interface](http://adslabs.org/adsabs/). I also showed some recent work that my student [Lukas Heinrich](http://www.lukasheinrich.com) has done to use GitHub webhooks to initiate requests to the [Recast](http://recast-demo.cern.ch) reintepretation framework (more on that in the [next post](/2015/05/Recast%20Progress/). After that I had to run to SFO to catch the red-eye to JFK. 