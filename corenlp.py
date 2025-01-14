from textblob import TextBlob
import wikipedia

def summarise_wikipedia(name):
    """return the summary from wikipedia"""

    print(f'obtaining the summary for {name}')
    return wikipedia.summary(name)

def get_text_blob(txt):
    """convert text to TextBlob"""

    blob = TextBlob(txt)
    return(blob)

def get_phrases(name):
    """return the noun phrases for a topic"""
    
    summary = summarise_wikipedia(name)
    blob = get_text_blob(summary)
    phrases = blob.noun_phrases
    return(phrases)