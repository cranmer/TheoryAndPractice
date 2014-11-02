Title: Searching for Cosmic Rays with Smart Phones
date: 2014-10-02 10:53
Slug: Crayfis
Category: Blog
Tags:  sabbatical, research, crayfis
Authors: Kyle Cranmer

It looks like I've joined another collaboration.


A few months ago my friend Daniel Whiteson told me about his crazy idea to use the cameras
in smart phones to detect ultra high energy [cosmic rays](http://en.wikipedia.org/wiki/Cosmic_ray). Sure, the CMOS sensor in your
cell phone is basically the same as the technology we use to track charged particles in
the ATLAS and CMS detectors at the LHC, but the sensor is tiny.  What are the chances
that a particle from a cosmic ray shower is going to hit that tiny camera?

<!--{% img  /images/cosmic_ray.jpg  305 %}{% img  /images/cosmic-rays.jpg  300 %}
-->
<div class="row">
	<div  class='col-md-6'> <img src="/images/cosmic_ray.jpg" width="100%" alt="a picture of a cosmic ray shower"></div>
	<div  class='col-md-6'> <img src="/images/cosmic-rays.jpg" width="100%" alt="a picture of a cosmic ray shower"></div>
</div>

That's an easy enough question to answer geometrically, but how do those cameras
really respond to cosmic rays? And what about the myriad of other questions you would need
to answer before making a case that you could actually do science this way? Well, that's 
exactly what Daniel Whiteson, Michael Mulhearn, Chase Shimmin, Kyle Brodie, and Dustin Burns
spent the summer doing. They wrote an app to run on a cell phone and then they put a
source of radiation close by to calibrate the efficiency with which these phones could detect charged particles. They also did some clever experiments with normal cosmic rays and some scintillator paddles. Not knowing if the entire idea was completely unrealistic or just wildly ambitious the group ran the numbers and put out a [paper](http://arxiv.org/abs/1410.2895). The upshot is that if we can get roughly a thousand clusters of a thousand users each, then this approach might be competitive with the big guys like [The Pierre Auger 
Cosmic Ray Observatory](http://www.auger.org) detector. A million users, sounds crazy -- just crazy enough to work :-)

<!--{% img 300 /images/crayfis_logo.png 300 %}-->

The project, called Crayfis now has a web page [http://crayfis.ps.uci.edu](http://crayfis.ps.uci.edu) and is accepting beta-testers. After a wave of media attention, the project now has more than 50,000 people signed up for beta testing. You can see up-to-date altmetrics below via [their api](https://api.altmetric.com/embeds.html), and click on the details to see an interesting "impact map". Importantly, you will see that Japan, with its high population density, seems to like the idea quite a bit.

<!--http://api.altmetric.com/embeds.html-->
<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>

<div class="row">
	<div  class='col-md-4'> <img src="/images/crayfis_logo.png" width="100%" alt="a picture of a cosmic ray shower"></div>
	<div  class='col-md-8'> 
		<div class='altmetric-embed' data-badge-type='donut' data-arxiv-id='1410.2895'
		data-badge-details='right' ></div>
	</div>
</div>


<!--<div class="row">
	<div  class='col-md-12'> 
		<div class='altmetric-embed' data-badge-type='donut' data-arxiv-id='1410.2895'
		data-badge-details='right' ></div>
	</div>
</div>-->

Since I'm on sabbatical at UCI, it was easy enough for me to see first-hand the lab
tests that the group had run and some more detailed plots. There are lots of questions,
like how the science is impacted by not having precise timing information like Auger does,
and the impact of over-burden for users running the app in their apartments. But so far there
are no obvious show stoppers.  So for the time being, I'm joining in this quixotic quest!

In addition to thinking about the science, the two main areas I'm pitching in are thinking
about how we would actually get this many users (social media, partnering with industry, 
etc.) and helping with the iPhone app. The current version of the app was written by Kyle 
Brodie -- an impressive undergraduate at UCI. Since he's busy with classes and we need to 
ramp up quickly, I'm taking lead the iOS development. So now I'm learning about the entirely
new world of iOS development, XCode, iTunes connect, TestFlight beta testing, etc. 




<!-- probably need some javascript for the guys below-->

<div class="fb-like" data-href="https://www.facebook.com/crayfisapp" data-layout="button" data-action="like" data-show-faces="true" data-share="true"></div>

<a href="https://twitter.com/crayfisapp" class="twitter-follow-button" data-show-count="false">Follow @crayfisapp</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>




