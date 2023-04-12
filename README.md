# check_tbx_entries
A script project to check a TBX-file for specific entries in the term-tag
To learn more about TBX-structure please find more information here: https://www.tbxinfo.net/

This is a training project, where I use chatGPT to create the scripts and then tweak them to my desire. I am still learning a lot about project structure and coding. Please feel free to participate or reuse the code.

A common problem in Terminology-Databases and company taxonomies are homographs (=the same sequence of letters mean different things in different context; for example). Therefor terminology checker in translation often encounter the problem that not the correct "concept"(German: "Begriff") are concerned and therefor you receive a lot of false-positives.

Together with a list of homographs that are common in certain domains and languages you can use this scrip to identify missing homographs in your terminology repository.

How could this be improved?
- integrate SpaCy and lemmatize terms in the TBX and the csv file and check if the lemmatized terms are matching each other
- check for compound terms (substrings) = a homograph might be a substring of a term in the tbx
