import pyaudio
import numpy as np
from time import sleep
from cypher import readableToCypher

#todo add as params
volume = 1
fs = 88200
duration = .5
spDuration = .1
f = 0
lo = 2200.0
two = 2400.0
three = 2600.0
four = 2800.0
five = 3000.0
freqs = [lo, two, three, four,five]
message="           123456789ABCDEF              "

p = pyaudio.PyAudio()

def playFreq():
   global f, fs, volume, sp, duration
   samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
   stream.write(volume * samples)

   
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

def prepareStr(st):
   r = ""
   for x in st:
      if x == " ":
         r+="0"
         continue
      if x in readableToCypher.keys():
         r+=readableToCypher[x] + "0"
   return r      
while True:
    for m in prepareStr(message):
        f = freqs[int(m)]
        playFreq()
stream.stop_stream()
stream.close()
p.terminate()
