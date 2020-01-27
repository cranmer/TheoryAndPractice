Title: Map of IRIS-HEP
date: 2020-01-25
Slug: collaboration-map-iris
Category: Blog
Tags: visualization
Authors: Kyle Cranmer
JavaScripts: d3.min.js, packages.js, collaboration-map.js, iris-collaboration-map-test.js
Stylesheets: concept-map.css, concept-map-padding.css

This is a variation on the other [Collaboration map](/2019/05/collaboration-map-iris/) aimed at IRIS-HEP.

 * people: with description that links to their homepage.
 * projects: specific projects or perhaps topics of discussion
 * collaborations: groups of people brought together with some common goal, theme, or for some other organizational reason 


## The result

<div id="graph" class="conceptmap" ></div>
<div id="graph-info"></div>

<br />


## Making it easier to make them with YAML

One nice thing about this appraoch is that the input to the D3.js script [is JSON](/downloads/files/collaboration.json) (here's an example on GitHub [link](https://github.com/cranmer/TheoryAndPractice/blob/javascript/content/downloads/files/test.json) ), so it should be easy to collaboratively guild this collaboration graph. However, the JSON is annoying to edit and the D3 script is picky. So I worked on a small script to convert a minimal YAML file into the corresponding JSON.

```python
import sys, yaml, json

def expand_dict(dict_in):
    dict_out = {}

    ditem_defaults = {'type':'ditem','links':[], 'description':''}
    dict_out['ditems'] = []
    n=0
    for i in dict_in['ditems']:
        n+=1
        for key in ditem_defaults.keys() - i.keys():
            i[key]=ditem_defaults[key]
        i['ditem']=n
        dict_out['ditems'].append(i)

    collab_defaults = {'type':'collaboration','description':'','group':1}
    dict_out['collaborations'] = []
    n=0
    for i in dict_in['collaborations']:
        n+=1
        for key in collab_defaults.keys() - i.keys():
            i[key]=collab_defaults[key]
        i['count']=n
        dict_out['collaborations'].append(i)

    proj_defaults = {'type':'project','description':''}
    dict_out['projects'] = []
    n=0
    for i in dict_in['projects']:
        n+=1
        for key in proj_defaults.keys() - i.keys():
            i[key]=proj_defaults[key]
        i['count']=n
        dict_out['projects'].append(i)
        
    return dict_out

#read files and convert
ydict_minimal={}
f = open('test_people.yml', 'r')
ydict_minimal.update(yaml.load(f))
f.close()
f = open('test_projects.yml', 'r')
ydict_minimal.update(yaml.load(f))
f.close()
f = open('test_colab.yml', 'r')
ydict_minimal.update(yaml.load(f))
f.close()

ydict_expanded = expand_dict(ydict_minimal)

f = open('test.json', 'w+')
json.dump(ydict_expanded,f,indent=1)
f.close()        
```

## Example YAML files

```yaml
ditems:
- name: Peter Elmer
  links:
  - CMS
  - DIANA
  - Executive Board
  - Steering Board
  - Innovative Algorithms
- name: Brian Bockelman
  links:
  - DOMA
  - DIANA
  - OSG
  - Executive Board
  - xcache
  - iDDS
  - third party copy
```

```yaml
projects:
- name: pyhf
- name: func_adl
- name: Coffea
- name: uproot
- name: Awkward Array
- name: Recast
- name: REANA
- name: MadMiner
- name: Scikit-Hep
```

```yaml
collaborations:
- name: ATLAS
- name: CMS
- name: LHCb
- name: DOMA
- name: Analysis Systems
- name: Innovative Algorithms
- name: SSL
- name: Blueprint
- name: Executive Board
- name: Steering Board
- name: Advisory Board
- name: Training, Education and Outreach
- name: OSG
- name: SCAILFIN
- name: DIANA
- name: DASPOS
```


- - - 

