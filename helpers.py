from gtts import gTTS 
import urllib.request 
import wikipedia as wp
from bs4 import BeautifulSoup
from creds import api_key
from google_images_download import google_images_download

def GenerateAudio(text):
    speech = gTTS(text = text, tld="co.uk",lang='en-gb',slow = False)
    speech.save("file.mp3")

def GetSummarizedText(topic):
    #url=f'https://simple.wikipedia.org/wiki/{topic}'
    #html = urllib.request.urlopen(url)
    #htmlParse = BeautifulSoup(html, 'html.parser')
    return wp.summary(topic, sentences = 5)

def downloadimages(query):
    for i in range(10):
        url=f"https://source.unsplash.com/1600x900/?{query}"
        urllib.request.urlretrieve(url, f"{i}.png")

#print(GetSummarizedText('programming'))
#downloadimages('cricket!')
