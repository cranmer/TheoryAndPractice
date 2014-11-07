Title: Searching for Cosmic Rays with Phones
date: 2014-10-02 10:53
Slug: Crayfis
Category: Blog
Tags:  sabbatical, research, crayfis
Authors: Kyle Cranmer

Some news... I've joined the Crayfis collaboration.


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
source of radiation close by to calibrate the efficiency with which these phones could detect charged particles. They also did some clever experiments with normal cosmic rays and some scintillator paddles, and they are even mooching off a muon test beam at CERN. Not knowing if the entire idea was completely unrealistic or just wildly ambitious the group ran the numbers and put out a [paper](http://arxiv.org/abs/1410.2895). The upshot is that if we can get roughly a thousand clusters of a thousand users each, then this approach might be competitive with the big guys like [The Pierre Auger 
Cosmic Ray Observatory](http://www.auger.org) detector in terms of exposure. A million users, sounds crazy -- just crazy enough to work :-)

<!--{% img 300 /images/crayfis_logo.png 300 %}-->

The project, called Crayfis now has a web page 
[http://crayfis.ps.uci.edu](http://crayfis.ps.uci.edu) and is accepting beta-testers. After 
a wave of media attention, the project now has more than 50,000 people signed up for beta 
testing. You can see up-to-date altmetrics below via [their api](https://api.altmetric.
com/embeds.html), and click on the details to see an interesting "impact map". Importantly, 
you will see that Japan, 
with its high population density, seems to like the idea quite a bit.

<!--
I'll be honest, there are a lot of open questions. In addition to the total "exposure", the 
Pierre Auger observatory has excellent timing information and a fluorescence detector that 
allows them to watch a cosmic ray shower develop in the atmosphere and time when the 
particles hit the ground. In contrast, the Crayfis approach does not have the timing
information for how a shower develops, which is a big loss. And there are lots of 
complications, like the phones being inside peoples apartments etc. At the same time,
if one could model that accurately, it might actually provide a new handle to photons
vs. muons. And the Crayfis array might have a much denser sampling around the core of 
the shower.  I also
love the notion that this world-wide detector might be sensitive to other things
as well. Imagine if multiple cosmic rays hit the Earth simultaneously... we are blind
to that now as far as I know. Or maybe it turns into  big radiation monitor, or something
else. Either way, it's such a cool idea I'm happy to be involved.
-->

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
tests that the group had run and some more detailed plots. I'll be honest, there are a lot of open questions. In addition to the total "exposure", the 
Pierre Auger observatory has excellent timing information and a fluorescence detector that 
allows them to watch a cosmic ray shower develop in the atmosphere and time when the 
particles hit the ground. In contrast, the Crayfis approach does not have the timing
information for how a shower develops, which is a big loss.
Similarly, there are complications from the over-burden for users running the 
app in their apartments. 
But I love the notion that this world-wide detector might be sensitive to other things
as well. Imagine if multiple cosmic rays hit the Earth simultaneously... we are blind
to that now as far as I know. Or maybe one ends up with a global monitoring of the 
muon flux that can be cross-correlated with weather and atmospheric conditions, which
could be useful for all sorts of things.  So for the time being, I'm joining in this 
quixotic quest!

In addition to thinking about the science, the two main areas I'm pitching in are thinking
about how we would actually get this many users (social media, partnering with industry, 
etc.) and helping with the iPhone app. The current version of the app was written by Kyle 
Brodie -- an impressive undergraduate at UCI. Since he's busy with classes and we need to 
ramp up quickly, I'm taking lead the iOS development. So now I'm learning about the entirely
new world of iOS development, XCode, iTunes connect, TestFlight beta testing, etc. 

If you are interested, sign up to be a beta tester [here](http://crayfis.ps.uci.edu/join.php). 

And you might want to follow one of the social media links for the Crayfis project:

<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.0";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

<div class="fb-like" data-href="https://www.facebook.com/crayfisapp" data-layout="button" data-action="like" data-show-faces="true" data-share="true"></div>

<a href="https://twitter.com/crayfisapp" class="twitter-follow-button" data-show-count="false">Follow @crayfisapp</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

---



