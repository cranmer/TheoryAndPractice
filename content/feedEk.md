Title: FeedEk
date: 2016-12-29
Slug: FeedEk
Category: Blog
Tags: visualization
Authors: Kyle Cranmer
JavaScripts:  https://code.jquery.com/jquery-1.9.1.min.js, FeedEk.js, FeedEk.min.js, test-FeedEk.js, test-FeedEk-minimal.js
Stylesheets: FeedEk.css


I've been a bit annoyed with [feed.mikle.com](https://feed.mikle.com/), the RSS feed widget I'm using on my homepage.
Sometimes it doesn't update, and while it is convenient, I can't modify the code to be able to tweak it. In particular, 
I'd like to get mathjax to work on the titles of the papers.

I was looking around earlier, and I found [FeedEK](http://jquery-plugins.net/FeedEK/FeedEK.html), which looks pretty nice.
Now that I've enabled [pelican_javascript](https://github.com/mortada/pelican_javascript), it's pretty easy. I did this first for the [Collaboration Map](/2016/12/collaboration-map/) and this time it only took me about five minutes to add the  [javascript](https://github.com/cranmer/TheoryAndPractice/tree/master/content/js) and [css](https://github.com/cranmer/TheoryAndPractice/tree/master/content/css). I'm pointing the feed to my INSPIRE profile: `http://inspirehep.net/rss?ln=en&p=a%3AK.S.Cranmer.1`. 

All I had to do in my markdown/html was add

```html
<div id="divRss"></div>
```


I'm still not sure how to get mathjax to render the LaTeX, but it seems more plausible now.

### Here's the minimal feed:

- - - 

<div id="divRss-minimal"></div>

### Here's the detailed feed:

- - - 

<div id="divRss"></div>
