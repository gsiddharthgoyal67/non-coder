#!usr/bin/python

import speech_recognition as SR

r=SR.Recognizer()

audio=SR.AudioFile("testtttt.wav")

with jackhammer as source:
    r.adjust_for_ambient_noise(source)
    AudioData=r.record(source,offset=2,duration=4)

type(AudioData)
text=r.recognize_google(AudioData)

print(text)

mic=SR.Microphone(device_index=7)
mic.list_microphone_names()


with mic as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)

# set up the response object
response = {
        "success": True,
        "error": None,
        "transcription": None
}

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
try:
    response["transcription"] = recognizer.recognize_google(audio)

except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

return response

ISaid=r.recognize_google(audio)

print("you said:"+ISaid)
