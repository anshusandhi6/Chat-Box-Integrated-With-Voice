import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
 
r = sr.Recognizer()
print("Hello!")
playsound("hello.mp3")

while 1:
    with sr.Microphone() as source :
        
        audio = r.listen(source, timeout = 10)
              
        try :
            speech = r.recognize_google(audio)
            print(speech.capitalize()) 
            
            if(speech == "ok bye") :
                break;

            reply = "k";
            voice_reply = gTTS(text = reply, lang='en')
            voice_reply.save("voice_reply.mp3")
            print(reply.capitalize())
            playsound("voice_reply.mp3")
            os.remove("voice_reply.mp3")
            
        except sr.UnknownValueError :
            print("Couldn't get what you said!")
            playsound("not_got.mp3")
            continue
            
        except Exception as e:
            print("error: {}".format(e))
            continue
        