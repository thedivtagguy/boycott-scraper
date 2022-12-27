# This contains a function which takes in a dataframe
# In the rawContent column, it finds all the links, hashtags, mentions and emojis
# And creates new columns for them
# If there are multiple links, hashtags, mentions or emojis, they are separated by a comma in the column

import re
import spacy as spacy
from clean_data import lower_case, trim_text


# Load the spacy model
nlp = spacy.load('en_core_web_sm')

# Function to get all named entities in a text and return them as a comma separated string
def get_named_entities(text):
    doc = nlp(text)
    named_entities = []
    for ent in doc.ents:
        named_entities.append(ent.text)

    named_entities_str = ",".join(named_entities)
    # Remove links, hashtags, mentions, numbers and punctuation (except commas and periods) from named entities
    named_entities_str = re.sub(r'https?://\S+|#\S+|@\S+|\b\d+\b|[^\s\w,.!?]', '', named_entities_str)
    return named_entities_str

def find_emojis(text):
  emoji_pattern = re.compile("["
        u"\U0001f600-\U0001f64f"  # emoticons
        u"\U0001f300-\U0001f5ff"  # symbols & pictographs
        u"\U0001f680-\U0001f6ff"  # transport & map symbols
        u"\U0001f1e0-\U0001f1ff"  # flags (iOS)
                           "]+", flags=re.UNICODE)
  emojis = emoji_pattern.findall(text)
  emojis_str = ",".join(emojis)
  return emojis_str

def clean_tweet(df):
    # Put all links in a comma separated list in a new column

    df['named_entities'] = df['rawContent'].apply(lambda x: get_named_entities(x))
    # Remove links, hashtags, mentions, numbers and punctuation (except commas and periods) from named entities
    df['named_entities'] = df['named_entities'].apply(lambda x: re.sub(r'(?:^|(?<=[^\s#@]))[^\s\w]+(?:$|(?=[^\s#@]))', '', x))

    df['links'] = df['rawContent'].apply(lambda x: ','.join(re.findall(r'http\S+', x)))


    # Put all hashtags in a comma separated list in a new column
    df['hashtags'] = df['rawContent'].apply(lambda x: ','.join(re.findall(r'#\S+', x)))
    df['hashtags'] = df['hashtags'].apply(lambda x: lower_case(x))
    df['hashtags'] = df['hashtags'].apply(lambda x: trim_text(x))


    # Put all mentions in a comma separated list in a new column
    df['mentions'] = df['rawContent'].apply(lambda x: ','.join(re.findall(r'@\S+', x)))

    return df
