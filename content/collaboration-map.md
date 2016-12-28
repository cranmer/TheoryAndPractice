Title: Collaboration Map
date: 2016-12-28
Slug: collaboration-map
Category: Blog
Tags: visualization
Authors: Kyle Cranmer
JavaScripts: d3.min.js, packages.js, collaboration-map.js, test-collaboration-map.js
Stylesheets: concept-map.css, concept-map-padding.css

For a long time I've wanted to come up with a nice way to visulize my collaborative network.
I've played with graphviz, but never been satisfied. I worked with Pablo Barberá 
last year to make something for our report for the [Moore-Sloan Data Science Initiative](http://msdse.org),
and we came up with this:

<img src="msdse-2015-collaboration-network.png" alt="MSDSE Collaboration Network" width="70%" />

It's ok, but it is lacking structur and semantics. I'd like to be able to visualize how people work
on common projects and how they are associated to different collaborations. This tends to be a 
many-to-many relationship.

### The Concept Map

While browsing the [d3 gallery](https://github.com/d3/d3/wiki/Gallery) I saw the 
[Concept network browser](http://www.findtheconversation.com/concept-map/), which I believe is from 
[Chris Willard](http://wllrd.com/). In addition to being visually striking and fun to play with, 
I liked how it has some semantic structure with people, themes, and perspectives. 

Many thanks to Xianshun Chen for making his [code](http://czcodezone.blogspot.com/2015/01/d3-simple-javascript-class-wrapper-for_25.html) for the concept map available.  I modified my [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) theme to use the 
[pelican_javascript](https://github.com/mortada/pelican_javascript) plugin. You can see how I 
arranged the [javascript](https://github.com/cranmer/TheoryAndPractice/tree/javascript/content/js)
and [css](https://github.com/cranmer/TheoryAndPractice/tree/javascript/content/css).

### A collaboration map

I decided to try to adapt the concept map to be a collaboration map. Initially I wanted to have people,
specific projects, and broad themes like physics, statistics, machine learning, software, cyberinfrastructure, etc. 
Maybe I'll come back to that, but for now I've decided to break it up into 
 * people: you know, like, people
 * projects: specific projects or perhaps topics of discussion
 * collaborations: groups of people brought together 

The visualization also allows one to group projects and collaborations, but the 


Not sure how to resize it yet. 

Ideally, I'd like to be able to enter the information in some JSON like form

I'm thinking of using this to describe my network of collaborators and projects.

<div id="graph" class="conceptmap" ></div>
<div id="graph-info"></div>
