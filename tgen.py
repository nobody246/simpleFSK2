import pyaudio
import numpy as np
from time import sleep
from cypher import readableToCypher
import signal
#todo add as params
volume = 1
fs = 88200
duration = .5 #can modify this value without changing rx code
f = 0
lo = 2200.0
two = 2400.0
three = 2600.0
four = 2800.0
five = 3000.0
freqs = [lo, two, three, four,five]
message="           THE_GRASS_IS_ALWAYS_GREENER_ON_THE_OTHER_SIDE_YANKEE_ALPHA_FOXTROT "
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
def sigHandler(s, fr):
   global p, stream
   stream.stop_stream()
   stream.close()
   p.terminate()     
   exit(0)
signal.signal(signal.SIGINT, sigHandler)
def playFreq():
   global f, fs, volume, sp, duration, stream
   samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
   stream.write(volume * samples)
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
