Title: Projects from July 2013
Date: 2013-07-13 02:38
Author: cranmer
Category: Blog
Tags: open science, physics, statistics, Communication
Slug: projects-from-july-2013

Wow, perhaps this is my first real blog post since rebooting
thoeryandpractice.org.  
And really one of my first blog posts ever.

I'm back from a really invigorating trip to CERN to give [some
statistics lectures to the CERN summer school][]. I played around with
[d3.js][], a cool javascript library for doing data visualization in the
browser. I also wanted to learn [flask][], a python based web
micro-framework. I got [my first non-trivial flask+d3 example going][]
and put it up here on [GitHub][]. Just to make my self super-trendy,
hipster, data scientist guy I also ditched emacs for [Sublime Text 2][].
This is actually a huge change given that I'm a power-user in emacs and
can do some pretty cool keyboard macros.

While I was there I met with Salvatore Mele and Sünje Dallmeier-Tiessen
from [INSPIRE][] and CERN open science initiatives. Some exciting things
on the front of presenting LHC results, perhaps publishing 2-d profile
likelihoods (slices of Higgs likelihoods in thousands of dimensions).
It's amazing how the model independent (cross-section)\_i x (branching
ratio)\_j contours (for i={VBF+WH, ggF+ttH} and j={WW, ZZ, γγ})

{% img //inspirehep.net/record/1241574/files/MuTMuW_comb_ggwwllll.png 400 "model independent presentation of Higgs couplings" %}


are sufficient statistics for for a number of benchmark-model coupling
measurements (eg. kV-kF, kg-kγ, λ\_WZ, etc.)

{% img //inspirehep.net/record/1241574/files/Model_CVCF_2D_CVCF_color_overlay.png 400 "Model-dependent coupling fits." %}

In addition, I just finished  the process of uploading data from
a [phenomenology paper I worked on a few years ago][] where we did a big
MCMC (Markov Chain Monte Carlo) scan of the CMSSM (Constrained Minimal
Supersymmetric Standard Model). So far I've uploaded it to both
[Figshare][] and to the [Harvard Dataverse Network][]. I think I'm going
to go with Dataverse though Figshare has been very nice. I'm choosing
Dataverse mainly b/c of attention to meta-data and ability to launch a
branded instances of the site. Though it did take me a hours to get the
upload to work and it only took about 10 seconds to upload it on
Figshare. Also, I want a nice API to tabular data so that I can link it
with [d3.js][]... neither have it, but FigShare's seems further behind
(surprisingly b/c they are much more "2.0"-ish).

So I've released my first dataset today (July 12, 2013) and it's here:

Cranmer, Kyle; Allanach, Ben; Lester, Christopher; Weber, Arne,
"Replication data for: "Natural Priors, CMSSM Fits and LHC Weather
Forecasts"", [hdl:1902.1/21804][] UNF:5:bvw2MoOATltX0yfGjF9hJQ== V1
[Version]

If you go to it and click on one of the TabularData entries you can even
do some minimal analysis from the web. Like this

![KISMET scan][]

I wish they would give me a little gist-style embed like this one:

<p>
<script type="text/javascript" src="https://gist.github.com/defunkt/202314.js"></script>
</p>
Anyways, that's a lot of playing around with new things of late. I hope
to see the [DataVerse handle][hdl:1902.1/21804] associated to [the
INSPIRE record][phenomenology paper I worked on a few years ago] soon.

  [some statistics lectures to the CERN summer school]: https://indico.cern.ch/conferenceDisplay.py?confId=243641
  [d3.js]: http://d3js.org
  [flask]: http://flask.pocoo.org
  [my first non-trivial flask+d3 example going]: http://flask.theoryandpractice.org
  [GitHub]: https://github.com/cranmer/flask-d3-hello-world
  [Sublime Text 2]: http://www.sublimetext.com
  [INSPIRE]: http://inspirehep.net
  []: http://inspirehep.net/record/1241574/files/MuTMuW_comb_ggwwllll.png
  [1]: http://inspirehep.net/record/1241574/files/Model_CVCF_2D_CVCF_color_overlay.png
  [phenomenology paper I worked on a few years ago]: http://inspirehep.net/record/749860
  [Figshare]: http://figshare.com
  [Harvard Dataverse Network]: http://thedata.org
  [hdl:1902.1/21804]: http://hdl.handle.net/1902.1/21804
  [KISMET scan]: http://theoryandpractice.org/wp-content/uploads/2013/07/KISMET-scan-300x187.png
