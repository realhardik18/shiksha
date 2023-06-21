from gtts import gTTS 

def GenerateAudio(text):
    speech = gTTS(text = text, tld="co.uk",lang='en-gb',slow = False)
    speech.save("file.mp3")

