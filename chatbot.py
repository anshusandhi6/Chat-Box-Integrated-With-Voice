import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import os
from new_predictions import predict_class, getResponse
from keras.models import load_model
import json

model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())

r = sr.Recognizer()

print("hello")
playsound("hello.mp3")

while 1:
    with sr.Microphone() as source :
        
        audio = r.listen(source)
              
        try :
            speech = r.recognize_google(audio)
            print(speech.capitalize())
            if(speech == "ok bye") :
                break;
             
            ints = predict_class(speech, model)
            reply = getResponse(ints, intents)
            print(reply)
            
            voice_reply = gTTS(text = reply, lang='en')
            voice_reply.save("voice_reply.mp3")
            
            playsound("voice_reply.mp3")
            os.remove("voice_reply.mp3")
            
        except sr.UnknownValueError :
            print("Couldn't get what you said!")
            playsound("not_got.mp3")
            continue
            
        except Exception as e:
            print("error: {}".format(e))
            continue
