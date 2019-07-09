import assemblyai

aai = assemblyai.Client(token=' 11fc9ccf99d040b5a831216a17556e4e')

transcript = aai.transcribe(filename='/home/adhoc/non-coder/aud.wav')


while transcript.status != 'completed':
    transcript = transcript.get()

text = transcript.text





