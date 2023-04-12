# check_tbx_entries
A script project to check a TBX-file for specific entries in the term-tag
To learn more about TBX-structure please find more information here: https://www.tbxinfo.net/

This is a training project, where I use chatGPT to create the scripts and then tweak them to my desire. I am still learning a lot about project structure and coding. Please feel free to participate or reuse the code.

A common problem in Terminology-Databases and company taxonomies are homographs (=the same sequence of letters mean different things in different context; in English there are many nouns that might be verbs in some instances). 

Terminology databases are used to collect the concepts of a domain with definitons and collect them in company or domain dictionaries. TBX is the internation standard exchange format for these type of data. These terminology data are used in translation context to assure the correct terms are applied during a translation and either the intellectual property or company desire is transported and misunderstandings are less common.

What many words have in common is that they can mean different things in different context. That means they are actually not the same word, but they are called homographs (if they are written identically) and homophones (if they sound identically but are written differently). 

Together with a list of homographs that are common in certain domains and languages you can use this script to identify missing homographs in your terminology repository.

How could this be improved?
- integrate SpaCy and lemmatize terms in the TBX and the csv file and check if the lemmatized terms are matching each other
- check for compound terms (substrings) = a homograph might be a substring of a term in the tbx
- the csv file containing homographs could be per language and thus reducing the amount of entries in the csv that are checked agains the xml
- the terms in the xml carry a language tag and could also be read depending on their language
- the result could contain the information per language

Additional checks on the tbx can be performed:
- have no entry start or end with a space
- have no double spaces in a term entry
