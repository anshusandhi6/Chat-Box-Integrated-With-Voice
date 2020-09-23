from gtts import gTTS
 
tts = gTTS(text="Couldn't get what you said!", lang='en')
tts.save("not_got.mp3")

print("Text Converted Successfully ")
