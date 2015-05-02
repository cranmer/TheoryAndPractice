Title: Recast Progress
date: 2015-5-01 14:53
Slug: Recast Progress
Category: Blog
Tags:  physics, open science
Authors: Kyle Cranmer




I'm pretty excited about the [Recast](http://recast-demo.cern.ch) reintepretation framework. The basic idea is that we want to capture the data processing pipeline associated with a search for new physics and then provide an API to it ([original paper](http://arxiv.org/abs/1010.2506) ). This will allow scientists outside the big LHC collaborations to request that a search be reinterpreted for their theory for new physics. Not only have we (read Lukas) made a lot of technical progress in prototyping this, but some similar ideas are popping up in other fields. Recently, F1000 Research has done some work on the [first living figure](http://f1000research.com/articles/3-176/v2) -- See articles [here](http://blog.f1000research.com/2015/04/22/first-living-scientific-figure-articles-can-now-keep-pace-with-scientific-discovery/) and [here](http://www.nature.com/news/living-figures-make-their-debut-1.17382
). 

One of the recent ideas from Arfon Smith was to use [GitHub webhooks](https://github.com/recast-hep/recast-github-webhooks/) to initiate pipeline processing. My student [Lukas Heinrich](http://www.lukasheinrich.com) pulled this off in a day, because he's awesome and these tools are really good.

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">Just demo’d using <a href="https://twitter.com/lukasheinrich_">@lukasheinrich_</a> GitHub Webhooks to initiate Recast requests: &#10;<a href="https://t.co/vkWRBjir9J">https://t.co/vkWRBjir9J</a>&#10;<a href="https://t.co/7OJ5KHyBEv">https://t.co/7OJ5KHyBEv</a></p>&mdash; Kyle Cranmer (@KyleCranmer) <a href="https://twitter.com/KyleCranmer/status/592862729758703616">April 28, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


I've also been thinking for a while about how to build the incentive structure around Recast, and one of the big ideas is that the request to the system should be considered the intellectual property of the person asking the question (usally a theorist) and the result should be considered the intellectual property of the experimental collaboration that collected the data and provided the data pipeline. The idea is that these new results would be appended to the original experiment's paper -- a bit like the living figure. I challenged Lukas to see if Lukas could interface with [Zenodo](http://zenodo.org) so that we can automatically mint DOIs for the data assocaited to the request/response, and he didn't disappoint! Here's the first example of a DOI for the output of a Recast request (this one is just for testing).

<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr">was really easy to integrate <a href="https://twitter.com/ZENODO_ORG">@ZENODO_ORG</a> with <a href="https://twitter.com/hashtag/recast?src=hash">#recast</a> thanks to great API. cc <a href="https://twitter.com/KyleCranmer">@KyleCranmer</a> <a href="http://t.co/05dBt9n1bM">pic.twitter.com/05dBt9n1bM</a></p>&mdash; Lukas Heinrich (@lukasheinrich_) <a href="https://twitter.com/lukasheinrich_/status/593464855702691842">April 29, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I'm excited to talk about these developments next week when I go to CERN for the [INSPIRE](http://inspirehep.net) and [HepData](http://hepdata.cedar.ac.uk) Advisory Board meetings.

