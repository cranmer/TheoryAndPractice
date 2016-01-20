Title:  Testing interactive blog post
date: 2016-01-18
Slug: Testing interactive blog post!
Category: Blog
Tags:  physics, machine learning, statistics
Authors: Kyle Cranmer

Recently I've been learning more about docker and all the things it can do for us.
My student Lukas Heinrich has been working on the [Recast](http://recast.perimeterinstitute.ca)
project and using docker heavily. In parallel, [Tim Head](http://betatim.github.io/) and I have
been talking a lot about projects like [binder](http://mybinder.org) and [everware](http://everware.xyz),
which let you run Jupyter notebooks in a GitHub repository with custom requirements encapsulated in 
a docker image. 

Most recently, Tim had [this awesome blog post](http://betatim.github.io/posts/really-interactive-posts/)
on interactive blog posts using static html. It's all powered via [`thebe`](https://github.com/oreillymedia/thebe).

I want to turn this example into one that uses a custom docker image that has [george](http://dan.iel.fm/george/current/)
installed, but so far I've not been successful with that. So just so I can feel like I've accomplished something,
here's an example from a recent blog post on [Hotelling's experiment](/2014/04/Hotelling-Experiment/).
The point here is that you have a static blog post that you can execute (and modify).
The last cell uses python2.7 syntax for the `print` statements in a python3 session, so it won't work.
But you can edit it accoridngly (comment out or change to `print(...)`.

Have fun, now let's embed the interactive notebook:

- - - 

{% thebe HotellingsExperiment.ipynb %}


