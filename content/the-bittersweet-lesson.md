Title:  The Bittersweet Lesson
date: 2025-09-17
Slug: The Bittersweet Lesson
Category: Blog
Tags:  physics, machine learning, AI 
Authors: Kyle Cranmer


In 2019, Rich Sutton authored an essay entitled “[The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)”, where he made the observation that general purpose methods that leverage computation eventually win over bespoke solutions that incorporate human domain knowledge. The essay has been the source of debate and evoked both positive and negative reactions. 

Within the AI for Science community, there is a strong instinct to incorporate domain knowledge as a form of inductive bias. It is intellectually gratifying and intuitively feels like the right thing to do from a learning perspective. After all, if we know (believe) there is some structure in the data, then it seems that reducing the model class can only help in terms of sample efficiency. Indeed, there are several examples where adding a well motivated form of inductive bias has improved performance and some examples where it has been an essential ingredient. 

At the same time, the AI for Science community is not blind to the rapid advances that are being made with large language models and multi-modal foundation models, where a very generic and general purpose strategy paired with massive data and compute is working extremely well. The number of “scaling laws” are proliferating, and the mantra ‘scale is all you need’ is taking hold. Fueling the fire are examples where removing well-motivated forms of inductive bias actually helped. 

Most of the debate around the bitter lesson is framed as a false dichotomy between two approaches. Sutton himself wrote “these two need not run counter to each other, but in practice they tend to.” The lesson that we should be taking from all of this is that we are confused. There is no consensus on which approach is better and there is conflicting evidence on the issue. But this confusion should be celebrated. It is progress. It’s the kind of bittersweet confusion that often precedes a major conceptual advance. Ideally, we would have a conceptual framework that could resolve the conflicting evidence and be a guide for the path forward.

For example, in theoretical chemistry problems that involve molecules there is no doubt that a rotational and translational symmetry exists *in silico*. Yet, paradoxically, there are examples where models that do not enforce this symmetry perform better than those that do. Why is that? I doubt that the restricted model class is the core of the problem. Instead, it seems likely that the way that model class is parametrized leads to a loss landscape that is challenging for our standard gradient-based learning algorithms or that they do not profit from phenomena that lead to good generalization in over-parametrized models. This is something to be understood. To dismiss this paradoxical situation as support for eschewing well-motivated forms of inductive bias is an opportunity lost. 

Sutton’s essay ends with the comment “We want AI agents that can discover like we can, not which contain what we have discovered.” Ironically, the quest for parsimonious representations, causal mechanisms, symmetries, and other manifestations of Occam’s razor is a key part of what it means to ‘discover like we can’. Instead of rejecting inductive bias outright, it seems that we should be working to understand how to incorporate the discovery of such structures into the learning algorithms themselves. 

In order to do so, we need better understanding of several key issues. In what situations do the forms of right inductive bias help in the long run? If they don’t help in the long run, can we understand better when and why there is a transition? If they should help in principle, but don’t help in practice, why is that? Are there fundamental advantages or disadvantages to encoding domain knowledge through data augmentation rather than at the architectural level?

The bittersweet lesson is that we are confused. But that confusion is a sign of progress. The path forward is to embrace the confusion and work to resolve it. With that in mind, one can reframe the efforts to build in known forms of inductive bias into models by hand not as an end goal, but as an intermediate step in a longer journey. These efforts and efforts like them can be used to inform those working to resolve the questions above.   



![]("/images/Kyle-Cranmer-Rich-Sutton-large.jpeg")
<div>
<img src="{filename}/images/Kyle-Cranmer-Rich-Sutton-large.jpeg" alt="Kyle Cranmer and Rich Sutton, September 16, 2025" width="90%" style="display: block; margin: auto;" />
<div style="text-align: center; font-style: italic;">Kyle Cranmer and Rich Sutton at the Heidelberg Laureate Forum, September 16, 2025. <br> Thumbs up does not indicate endorsement of this essay.</div>
</div>

-----

*Note*: After writing this essay and [sharing the the working title publicly](https://youtu.be/I-Ye-rMhRws?si=t-iRuTE8cnxGNAaa&t=5203), I came across an [essay](
https://medium.com/@felixhill/the-agreeable-lesson-9766382c6d83) by Felix Hill with the same name (though the blog URL is "the agreeable lesson"). Felix's essay is also in response to Sutton's essay, but it takes a different perspective. I recommend reading it as well. 
