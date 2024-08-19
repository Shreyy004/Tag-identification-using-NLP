import urllib.request # handling URL
from bs4 import BeautifulSoup # handling or parsing HTML files
import nltk # toolkit
nltk.download('stopwords') # downloading stopwords

from nltk.corpus import stopwords

# Get the info from website
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Tata_Group')
html = response.read()
# print(html)  # Uncomment this if you want to see the HTML content

# Removes tags and groups into tokens - separate strings
soup = BeautifulSoup(html, 'html5lib')
text = soup.get_text(strip=True)
# print(text)  # Uncomment this if you want to see the extracted text

tokens = [t for t in text.split()]
# print(tokens)  # Uncomment this if you want to see the tokens

# Remove stop words from tokens
sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in sr:
        clean_tokens.remove(token)

# print(clean_tokens)  # Uncomment this if you want to see the clean tokens

# Calculate frequency distribution of the clean tokens
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(f'{key}: {val}')
freq.plot(20)
