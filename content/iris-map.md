Title: Map of IRIS-HEP
date: 2019-05-05
Slug: collaboration-map-iris
Category: Blog
Tags: visualization
Authors: Kyle Cranmer
JavaScripts: d3.min.js, packages.js, collaboration-map.js, iris-collaboration-map.js
Stylesheets: concept-map.css, concept-map-padding.css

This is a variation on the other [Collaboration map](/2016/12/collaboration-map/) aimed at IRIS-HEP.

 * people: with description that links to their homepage.
 * projects: specific projects or perhaps topics of discussion
 * collaborations: groups of people brought together with some common goal, theme, or for some other organizational reason 

One nice thing about this appraoch is that the [input is JSON](/downloads/files/collaboration.json) (here's an example on GitHub [link](https://github.com/cranmer/TheoryAndPractice/blob/javascript/content/downloads/files/collaboration.json) ), so it should be easy to collaboratively guild this collaboration graph. 

I'd like to make something easier to edit with yaml and then convert it to JSON, but I'll leave that for another day.

The interactive visualization at the top is my first try at a collaboration map. 


<div id="graph" class="conceptmap" ></div>
<div id="graph-info"></div>

<br />
- - - 

