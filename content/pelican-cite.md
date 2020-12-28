Title:  Citing from a bibtex file
date: 2020-12-27
Slug: pelican-cite
Category: Blog
Tags:  website
Authors: Kyle Cranmer
Stylesheets: pelican-cite.css

I've been wanting to add some semi-automated way to handle papers and bibliography information in this website. I found [pelican-bibtex](https://github.com/vene/pelican-bibtex) and [pelican-cite](https://github.com/VorpalBlade/pelican-cite). I'll need to look into pelican-bibtex to see if I can make a nice automated page based on a `.bib` file, but pelican-cite looked pretty easy to setup. 

Ok, let's see how this works. I got the .bib file from INSPIRE [here](https://inspirehep.net/literature?sort=mostrecent&size=25&page=1&q=a%3Ak.s.cranmer.1&author_count=10%20authors%20or%20less&ui-citation-summary=true).

I am doing a simple `grep "@" content/kyle-10authors-2020.bib ` and then I can use a keyboard macro in VS Code to get the necessary markdown, which should complete into a nicer looking reference. Here are the papers with less than 10 authors that I wrote in 2020: 

[@Brehmer:2020ako]
[@Brehmer:2020brs]
[@Mishra-Sharma:2020kjb]
[@Brehmer:2020cvb]
[@Boyda:2020hsi]
[@Shlomi:2020ufi] 
[@Cranmer:2020wew]
[@Brehmer:2020zwh]
[@Brehmer:2020vwc]
[@Kanwar:2020xzo]
[@Greenberg:2020heb]
[@Serviansky:2020qwa]
[@Rezende:2020hrd]

Well, I had to edit some entries in the `.bib` file that had missing `journal` information or it lead to a critical failure. This is nice, but not exactly what I'm looking for. 

... time passes...

Ok, I played with [pelican-bibtex](https://github.com/vene/pelican-bibtex) some. I added a custom template and I hacked pelican-bibtex with this:

``` 
    #hack added by Kyle Cranmer to avoid problems in bib with no journal entry
    for entry in bibdata_all.entries.values():
        if 'journal' not in entry.fields: 
            entry.fields['journal']=''
        if 'booktitle' not in entry.fields: 
            entry.fields['booktitle']=''

    formatted_entries = plain_style.format_entries(bibdata_all.entries.values())
```
so that I don't have to modify the `.bib` file. That produces [this page](/publications.html)