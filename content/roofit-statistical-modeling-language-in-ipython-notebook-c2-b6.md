Title: RooFit statistical modeling language demo in an iPython notebook
Date: 2014-03-04 21:01
Author: cranmer
Category: Blog
Slug: roofit-statistical-modeling-language-in-ipython-notebook%c2%b6

Particle physicisits primarily use [ROOT][] for the data analysis
framework. Part of that framework is a package
called [RooFit][] statistical modeling and fitting package. I have
contributed to this package and added a layer on top
called [RooStats][] that provides with statistical inference in both
frequentist and Bayesian paradigms based on statistical models made with
RooFit. These are the tools that were used to claim the discover the
Higgs boson, and those [statistical models get pretty complicated][].

<span style="line-height: 1.5em;">I created</span>[a little iPython
notebook to demonstrate a simple example of RooFit's ability][]<span
style="line-height: 1.5em;"> to create a statistical model, generate
some simulated data, fit that data, create the profile likelihood, and
provide a covariance matrix from the likelihood fit.  Enjoy!</span>

  [ROOT]: http://root.cern.ch/
  [RooFit]: http://root.cern.ch/drupal/content/users-guide#roofit
  [RooStats]: https://twiki.cern.ch/twiki/bin/view/RooStats/WebHome
  [statistical models get pretty complicated]: http://blogs.discovermagazine.com/cosmicvariance/2011/12/08/making-the-higgs-sausage/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+CosmicVariance+%28Cosmic+Variance%29#.UxFW0NyrvlI
  [a little iPython notebook to demonstrate a simple example of RooFit's
  ability]: http://nbviewer.ipython.org/github/cranmer/play/blob/master/iPythonROOT/BasicRooFitExample.ipynb
