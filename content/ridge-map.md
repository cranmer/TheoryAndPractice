Title:  RidgeMap
date: 2019-05-05
Slug: RidgeMap
Category: Blog
Tags:  python, visualization
Authors: Kyle Cranmer

The other day I saw this tweet:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Inspired by <a href="https://twitter.com/ZachACole?ref_src=twsrc%5Etfw">@ZachACole</a>&#39;s beautiful illustrations and <a href="https://twitter.com/jakevdp?ref_src=twsrc%5Etfw">@jakevdp</a>&#39;s pulsar plots, I just released a library to make &quot;ridge elevation plots&quot; with Python and <a href="https://twitter.com/matplotlib?ref_src=twsrc%5Etfw">@matplotlib</a>. Let me know if you make something nice! <a href="https://t.co/X3XLnA6qAM">https://t.co/X3XLnA6qAM</a> <a href="https://t.co/UfApYUDTH8">pic.twitter.com/UfApYUDTH8</a></p>&mdash; Colin Carroll (@colindcarroll) <a href="https://twitter.com/colindcarroll/status/1123569652582506498?ref_src=twsrc%5Etfw">May 1, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


And then had the idea to make a couple as a birthday gift for my Dad.
So I installed Colin Carroll's awesome [RidgeMap tool](https://github.com/ColCarroll/ridge_map), went over to [boxfinder](http://bboxfinder.com/#34.712831,-92.673368,34.745844,-92.624016), worked a bit [to get the fonts right](https://github.com/ColCarroll/ridge_map/issues/7) and ended up with this:


{% notebook downloads/notebooks/LakeNorrel.ipynb %}


Here's the area in google maps


<div class="row">
    <div class="centered text-center">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13115.775435892076!2d-92.65505226818304!3d34.73180946985931!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x87cd44905576d125%3A0xe926acac72633f42!2sLake+Norrell!5e0!3m2!1sen!2sus!4v1557187379507!5m2!1sen!2sus" width="600" height="450" frameborder="0"  style="border:0" allowfullscreen></iframe>
    </div>
</div>