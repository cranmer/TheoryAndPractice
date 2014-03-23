Title: Inspired by the Higgs, a step forward in open access
Date: 2013-09-13 13:31
Author: cranmer
Category: Blog
Tags: higgs, physics, open science
Slug: inspired-by-the-higgs-a-step-forward-in-open-access

[originally posted on [Quantum Diaries][]]

The discovery of the Higgs boson is a major step forward in our
understanding of nature at the most fundamental levels. In addition to
being the last piece of the standard model, it is also at the core of
the fine tuning problem -- one of the deepest mysteries in particle
physics. So it is only natural that our scientific methodology rise to
the occasion to provide the most powerful and complete analysis of this
breakthrough discovery.

 

This week the ATLAS collaboration has taken an important step forward by
making the likelihood function for three key measurements about the
Higgs available to the world digitally. Furthermore, this data is being
shared in a way that represents a template for how particle physics
operates in the fast-evolving world of open access to data. These steps
are a culmination of decades of work, so allow me to elaborate.

 
{% img //www.quantumdiaries.org/wp-content/uploads/2013/09/Higgs-production-horizontal.png 500  "Four interactions that can produced a Higgs boson at the LHC" %}
 

First of all, what are the three key measurements, and why are they
important? The three results were presented by ATLAS in [this recent
paper][]. Essentially, they are measurements for how often the Higgs is
produced at the LHC through different types of interactions (shown
above) and how often it decays into three different force carrying
particles (photons, W, and Z bosons). In this plot, the black + sign at
(1,1) represents the standard model prediction and the three sets of
contours represent the measurements performed by ATLAS. These
measurements are fundamental tests of the standard model and any
deviation could be a sign of new physics like supersymmetry!

{% img //www.quantumdiaries.org/wp-content/uploads/2013/09/fig_07.png 400 "Higgs production and decay measured by ATLAS." %}


Ok, so what is the likelihood function, and why is it useful? Here maybe
it is best to give a little bit of history. In 2000, [the first in a
series of workshops][] was held at CERN where physicists gathered to
discuss the details of our statistical procedures that lead to the final
results of our experiments. Perhaps surprisingly, there is no unique
statistical procedure, and there is a lot of debate about the merits of
different approaches. After a long discussion panel, Massimo Corradi cut
to the point

> It seems to me that there is a general consensus that what is really
> meaningful for an experiment is likelihood, and almost everybody would
> agree on the prescription that experiments should give their
> likelihood function for these kinds of results. Does everybody agree
> on this statement, to publish likelihoods?

And as Louis Lyons charred the session...

> Any disagreement? Carried unanimously. That's actually quite an
> achievement for this workshop.

So there you have it, the likelihood function is the essential piece of
information needed for communicating scientific results.

So what happened next? Well... for years, despite unanimous support,
experiments still do not publish their likelihood functions. Part of the
reason is that we lacked the underlying technology to communicate these
likelihood functions efficiently. In the run up to the LHC we developed
some technology (associated to RooFit and RooStats) for being able to
share [very complicated likelihood functions][] internally. This would
be the ideal way to share our likelihood functions, but we aren't quite
there yet. In January 2013, we had [a conference devoted to the topic of
publishing likleihood functions][], which culminated in a paper ["On the
presentation of LHC Higgs results"][]. This paper, written by theorist
and experimentalists, singled out the likelihood associated to the plot
above as the most useful way of communicating information about the
Higgs properties.

{% img //www.quantumdiaries.org/wp-content/uploads/2013/09/Test-kVkF-contours.png 400  "An overlay of the original ATLAS result (filled contours) and those reproduced from the official ATLAS likelihood functions." %}

The reason that these specific Higgs plots are so useful is that more
specific tests of the standard model can be derived from them. For
instance, one might want to consider beyond the standard model theories
where the Higgs interacts with all the matter particles (fermions) or
all the force carrying particles (vector bosons) differently than in the
standard model. To do that, it is useful to group together all of the
information in a particular way and take a special 2-d slice through the
6-d parameter space described by the three 2-d plots above. To the left
is the result of this test (where the axes are called κ\_F and κ\_V for
the vector bosons and fermions, respectively). What is special about
this plot is that there is an overlay of the original ATLAS result
(filled contours) and those reproduced from the official ATLAS
likelihood functions. While my student Sven Kreiss made the comparison
as part of a test, anyone can now reproduce this plot from the official
ATLAS likelihood functions. More importantly, the same procedure that
was used to make this plot can be used to test other specific theories
-- and there are a lot of alternative ways to reinterpret these Higgs
results.

Great! So where can you find these likelihood functions and what does
this have to do with open access? I think this part is very exciting.
CERN is now famous for being the [birthplace for the world wide web][]
and having a forward-looking [vision for open access][] to our published
papers. The sheer volume and complexity of the LHC data makes the
conversation about open access to the raw data quite complicated.
However, having access to our published results is much less
controversial. While it is not done consistently, there are several
examples of experiments putting information that goes into tables and
figures on [HepData][] (a repository for particle physics measurements).
Recently, our literature system [INSPIRE][] started to integrate with
HepData so that the data are directly associated to the original
publication (here is an [example][]). What is important is that this
data is discoverable and citable. If someone uses this data, we want to
know exactly what is being used and the collaborations that produced the
data deserve some credit. INSPIRE is now issuing a [Digital Object
Identifier][] (DOI) to this data, which is a persistent and trackable
link to the data.

So now for the fun part, you can go over to the INSPIRE record for the
recent Higgs paper (<http://inspirehep.net/record/1241574>) and you will
see this:

{% img //www.quantumdiaries.org/wp-content/uploads/2013/09/Inspire-record-higgs.png 600 "The INSPIRE record for the recent ATLAS Higgs paper." %}

If you click on [HepData tab][] at the top it will take you to a list of
data associated to this paper. Each of the three entries has a DOI
associated to it (and lists all the ATLAS authors). For example, the
H→γγ result's DOI is [10.7484/INSPIREHEP.DATA.A78C.HK44][], and this is
what should be [cited][] for any result that uses this likelihood.
(Note, to get to the actual data, you click on the Files tab.) INSPIRE
is now working so that your author profile will not only include all of
your papers, but also the data sets that you are associated with (here's
an[example][1] in it's early form based on [my ORCID ID][]).


{% img //www.quantumdiaries.org/wp-content/uploads/2013/09/INSPIRE-H-gamgam.png 600 "The H to two photon likelihood function." %}

Now it's time for me and my co-authors to update our paper ["On the
presentation of LHC Higgs results"][] to cite this data. And next week,
Salvatore Mele, head of Open Access at CERN, will give a [keynote
presentation][] to the DataCite conference entitled "A short history of
the Higgs Boson. From a tenth of a billionth of a second after the Big
Bang, through the discovery at CERN, to a DataCite DOI".

I truly hope that this becomes standard practice for the LHC. It is a
real milestone for the information architecture associated to the field
of high energy physics and a step forward in the global analysis of the
Higgs boson discovered at the LHC!

  [Quantum Diaries]: http://www.quantumdiaries.org/2013/09/12/inspired-by-the-higgs-a-step-forward-in-open-access/
  [this recent paper]: http://inspirehep.net/record/1241574
  [the first in a series of workshops]: https://cds.cern.ch/record/411537?ln=en
  [very complicated likelihood functions]: http://blogs.discovermagazine.com/cosmicvariance/2011/12/08/making-the-higgs-sausage/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+CosmicVariance+%28Cosmic+Variance%29#.UjCw8RYZ6uA
  [a conference devoted to the topic of publishing likleihood functions]: http://indico.cern.ch/conferenceDisplay.py?confId=218693%20
  ["On the presentation of LHC Higgs results"]: http://inspirehep.net/record/1244142%20
  [birthplace for the world wide web]: http://home.web.cern.ch/about/birth-web
  [vision for open access]: http://library.web.cern.ch/oa/policy
  [HepData]: http://hepdata.cedar.ac.uk
  [INSPIRE]: http://inspirehep.net/
  [example]: http://inspirehep.net/record/1228693/hepdata
  [Digital Object Identifier]: http://www.doi.org
  [HepData tab]: http://inspirehep.net/record/1241574/hepdata
  [10.7484/INSPIREHEP.DATA.A78C.HK44]: http://doi.org/10.7484/INSPIREHEP.DATA.A78C.HK44
  [cited]: http://inspirehep.net/record/1253646/export/hx
  [1]: https://inspirehep.net/search?ln=en&cc=Data&p=100%3A+0000-0002-5769-7094&action_search=Search
  [my ORCID ID]: http://orcid.org/0000-0002-5769-7094
  [keynote presentation]: http://datacite.eventbrite.co.uk
