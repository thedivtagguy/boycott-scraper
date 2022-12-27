import re

def clean_text(text):

  # remove non-ASCII characters
  text = re.sub(r'[^\x00-\x7F]+', '', text)
  
  # lowercase the text
  text = text.lower()
  
  
  # remove punctuation but not hashtags, mentions and links
  text = re.sub(r'(?:^|(?<=[^\s#@]))[^\s\w]+(?:$|(?=[^\s#@]))', '', text)
  # Remove anything with https
  text = re.sub(r'https\S+', '', text)
  
  # remove extra whitespaces
  text = re.sub(r'\s+', ' ', text).strip()
  
  # remove stopwords
  from nltk.corpus import stopwords
  stop_words = stopwords.words('english')
  text = ' '.join([word for word in text.split() if word not in stop_words])
  
  # lemmatize the text
  from nltk.stem import WordNetLemmatizer
  lemmatizer = WordNetLemmatizer()
  text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
  
  return text

def lower_case(text):
  text = text.lower()
  return text

def trim_text(text):
  text = text.strip()
  return text
