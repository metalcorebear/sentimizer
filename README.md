# Sentimizer

## About

Sentimizer will measure sentiment around specific entities within text.  It is built on NLTK, Spacy, and NRCLex.  Output is a dictionary that can be analyzed further, graphed, formulated into a wordcloud, etc.

## References
* https://github.com/explosion/spaCy
* https://github.com/nltk
* https://github.com/metalcorebear/NRCLex

## Revision History
* 2022-10-17: initial commit.

## Example Usage
`pip install sentimizer`

### Instantiate SentiMizer Object
`from sentimizer import SentiMizer`<br><br>
`analyzer = SentiMizer()`

### Load Text
Loads initial body of text.<br><br>
`analyzer.load_text(text : str)`<br><br>
`analyzer.text` - attribute contains loaded text (str).

### Append Text
For appending additional text to the initial input.<br><br>
`analyzer.append_text(text : str)`

### Entity Recognition
For identifying entities within the loaded body of text.<br><br>
`analyzer.find_entities()`<br><br>
optional parameters:<br><br>
`entity_types_of_interest` - list of entity types for recognition.  Default value is `['ORG', 'PERSON', 'FAC', 'GPE', 'LOC', 'EVENT']`  All possible lables include: `CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART` For a description of each, visit https://spacy.io/models/en. <br><br>
`analyzer.entities` - dictionary of entities and their tags (dict).<br><br>
`analyzer.sentences` - dictionary of entities and concatenated sentences containing each entity (dict).  Keys are entities and values are the concatenated sentences mentioning that entity.

### Measure Emotional Content
For measuring sentiment and emotional affect of sentences that mention each entity.<br><br>
`analyzer.emote()`<br><br>
`analyzer.sentiments` - Vader composite sentiment scores for each entity (dict).  Keys are entities and values are the composite sentiment score for that entity.<br><br>
`analyzer.affect` - NRCLex affect scores for each entity (dict).  Keys are entities and the values are affect frequency dictionaries.