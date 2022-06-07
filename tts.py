import gtts 
import os
from playsound import playsound
text=input()
t1 = gtts.gTTS(text=text, slow=False) 
t1.save("t2s.mp3")
t1.save("t2s.wav")
playsound("t2s.mp3")
