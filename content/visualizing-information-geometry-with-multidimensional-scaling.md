Title: Visualizing information geometry with multidimensional scaling
Date: 2014-03-22 16:47
Author: cranmer
Category: Blog
Tags: Data, python, Statistics
Slug: visualizing-information-geometry-with-multidimensional-scaling


This weekend's project was a fun one!  

_Update: Since the original post I made some more progress. I'm developing the code into my GitHub [play/manifoldLearning](https://github.com/cranmer/play/tree/master/manifoldLearning) repository.  Below is from the README._

- - -

I'm working on a paper about Informtion Geometry.  
The first step was an iPython notebook on [Visualizing information geometry with multidimensional scaling](http://nbviewer.ipython.org/github/cranmer/play/blob/master/manifoldLearning/GaussianInformationGeometryEmbedding.ipynb). 

The other python files are me working my way to something more ambitious.

**Step 1:**
The first step is described nicely in this iPython notebook on [Visualizing information geometry with multidimensional scaling](http://nbviewer.ipython.org/github/cranmer/play/blob/master/manifoldLearning/GaussianInformationGeometryEmbedding.ipynb). Final result shown here. Important part is a grid of points in (μ,σ) being mapped by f:

{% img /images/gaussianInfoGeom.png 400 %}

**Step 2:**
Try various [scikit-learn](http://scikit-learn.org/0.11/modules/generated/sklearn.svm.SVR.html) algorithms, setteling on NuSVR. Results not so good, smaller red spots not approximating the larger colorful training samples, particuarly near the edges. The lower-right is what I'm ultimately after, the inverse map of back into the space (μ,σ) -- for these points, that should be a perfect grid. Surprised I can't do regression on 

{% img /images/learnEmbedding.png 400 %}


**Step 3:**
Since this is a low dimensional problem with little noise, just try [SciPy Interpolation](http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html#d-interpolation-interp1d) algorithms. Ah, that's better, now I'm getting the grid I want.

{% img /images/interpEmbedding.png 400 %}

**Step 4:**
To do: make a regular grid in the target space and project it via the inverse into the (μ,σ) plane.  This is a "smart" sampling from an information theoretic perspective. It's also a good choice if simulation of the statistical model is expensive (ie. full simulation with GEANT at the LHC, which takes about 20 min per event, and the real collisons are happening at 40 million/sec. )

**Step 5:**
To do: repeat exercise with MSSM SUSY grids published on HepData. Change from Gaussian to Poisson, where I can still solve for the information distance analytically. Repeat steps 3 & 4 for that case, evaluate embedding from information persepctive, and propose a better choice for the parameter scan "grids" used by the ATLAS collaboration.

**Step 6:**
To do: move to a non-number counting model, generate graph of KL distances, use shortest path on this graph (via Dijkstra's algorithm) to approximate the geodesic from the fisher information metric -- perhaps using [boost libraries](http://www.boost.org/doc/libs/1_55_0/libs/graph/doc/index.html) or the code from [FINE](http://arxiv.org/abs/0802.2050), amazingly [the code is available](http://tbayes.eecs.umich.edu/kmcarter/fine_doc) -- nicely done Kevin Carter!

For convenience, the original notebook is embedded below (using the pelican liquid notebook plugin)

- - - 

{% notebook downloads/notebooks/GaussianInformationGeometryEmbedding.ipynb %}