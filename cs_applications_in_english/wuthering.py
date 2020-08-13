# Sentiment analysis on the piece of classic literature:
# Wuthering Heights. For more information on nltk functions
# and other Natural Language Processing Toolkit Applications
# please visit https://www.nltk.org/. Happy coding!

import nltk
from urllib import request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('punkt')

#pre-processing to grab text
url = "https://www.gutenberg.org/files/768/768.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)

#concordance of the text file - print automatically
text.concordance("moors")

#common-contexts of where words appear - print automatically
text.common_contexts(["moors"])
text.common_contexts(["Cathy", "Heathcliff"])

#word frequency and percentage
count_heathcliff = text.count("Heathcliff")
print(count_heathcliff)
total_words = len(text)
percentage_heathcliff = count_heathcliff/total_words
print(percentage_heathcliff)

#sentiment analysis
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()
scores = sid.polarity_scores(raw)
print(scores)
