Title:  INSPIRE API
date: 2019-04-14
Slug: INSPIRE API
Category: Blog
Tags:  python
Authors: Kyle Cranmer


For the [IRIS-HEP](http://iris-hep.org) organization we need to collect publications and update our webpage regularly. I also have to do this for our group webpage, my CV, etc. It's annoying to copy/paste all of this information. The [http://inspirehep.net](INSPIRE) website lets you export bibtex, latex, and plain text for individual papers or a set of papers that match a search result, but it's still not very convenient for web stuff where Markdown is common. The IRIS-HEP webpage is also based on jekyll, and can parse yaml files for making publication pages. So I wanted a tool that could ingest a bunch of paper identifiers and output yaml.

The new [INSPIRE beta](https://labs.inspirehep.net) has a more modern API, so I wanted to try that out. Here's a [repo](https://github.com/cranmer/inspire_play) with what I came up with while at CERN

```python
recid_unpublished = 1726790 #notpublished
recid_published = 1705857 #published
list_of_recids = [recid_published, recid_unpublished]
yaml.dump(summarize_records(list_of_recids),default_flow_style=False)
```

which yields

```yaml
publications:
- arxiv_eprint: '1811.12113'
  authors: Aaboud, Morad; Aad, Georges; Abbott, Brad; Abdinov, Ovsat; Abeloos, Baptiste;
    et. al.
  collaboration: ATLAS
  creation_date: '2018-11-30'
  doi: 10.1007/JHEP04(2019)046
  journal_title: JHEP
  journal_volume: '04'
  journal_year: 2019
  page_start: '046'
  recid: 1705857
  title: Measurements of fiducial and differential cross-sections of $t\bar{t}$ production
    with additional heavy-flavour jets in proton-proton collisions at $\sqrt{s}$ =
    13 TeV with the ATLAS detector
  url: https://arxiv.org/abs/1811.12113
- arxiv_eprint: '1903.10563'
  authors: Carleo, Giuseppe; Cirac, Ignacio; Cranmer, Kyle; Daudet, Laurent; Schuld,
    Maria; et. al.
  creation_date: '2019-03-27'
  recid: 1726790
  title: Machine learning and the physical sciences
  url: https://arxiv.org/abs/1903.10563
```

Here's an except from the notebook

{% notebook downloads/notebooks/inspire-try1.ipynb cells[0:9] %}


<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Hacking in the sun in the on the <a href="https://twitter.com/CERN?ref_src=twsrc%5Etfw">@CERN</a> patio while jet lagged.<br> - Input: <a href="https://twitter.com/inspirehep?ref_src=twsrc%5Etfw">@inspirehep</a> record IDs<br> - Output: yaml for <a href="https://twitter.com/iris_hep?ref_src=twsrc%5Etfw">@iris_hep</a> webpage<br> - Bonus: try it on Binder thanks to <a href="https://twitter.com/mybinderteam?ref_src=twsrc%5Etfw">@mybinderteam</a> <br> - code: <a href="https://t.co/9FKalW43oM">https://t.co/9FKalW43oM</a> <a href="https://t.co/AxatW6YiJP">pic.twitter.com/AxatW6YiJP</a></p>&mdash; Kyle Cranmer (@KyleCranmer) <a href="https://twitter.com/KyleCranmer/status/1117374674697060352?ref_src=twsrc%5Etfw">April 14, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
