#!/usr/bin/env python
import pyaudio
from numpy import zeros,linspace,short,fromstring,hstack,transpose
from scipy import fft
from time import sleep, time
from cypher import cypherToReadable
import signal
SENSITIVITY= 0.1
BANDWIDTH = 100
SAMPLES = 1024
RATE = 88200
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=SAMPLES)
def sigHandler(s, fr):
   global pa, stream
   stream.stop_stream()
   stream.close()
   pa.terminate()     
   exit(0)
signal.signal(signal.SIGINT, sigHandler)
lo = 2200.0
two = 2400.0
three = 2600.0
four = 2800.0
five = 3000.0
DETECT = [lo, two, three, four,five]
scores = [0,0,0,0,0]
scoreIndex = 0
curChr = ""
lastChr=""
msg = ""
lastIndex = None
showErrors = False
def processMsg(m):
   global showErrors
   c = ""
   for x in m.split("0"):
      n = ""
      l = ""
      for y in x:
         if y == l:
            continue
         n+=y
         l = y
      if n in cypherToReadable.keys():
         c+=cypherToReadable[n]
      elif showErrors:
         c+="[X] "
   print c
spCnt = 0
sigFound = False
print "listening for code.."
while True:
   while stream.get_read_available()< SAMPLES: sleep(0.005)
   audioData  = fromstring(stream.read(
         stream.get_read_available()), dtype=short)[-SAMPLES:]
   normalizedData = audioData / 32768.0
   intensity = abs(fft(normalizedData))[:SAMPLES/2]
   frequencies = linspace(0.0, float(RATE)/2, num=SAMPLES/2)
   maxScoreIndex = scores.index(max(scores))
   maxScore = max(scores)
   for tone in DETECT:
      try:
          if max(intensity[(frequencies < tone+BANDWIDTH) &
                           (frequencies > tone-BANDWIDTH )]) >\
             max(intensity[(frequencies < tone-1000) &
                           (frequencies > tone-2000)]) + SENSITIVITY:
              scoreIndex = DETECT.index(tone)
              scores[scoreIndex] += 1
              if lastIndex != scoreIndex and maxScore >= 2:
                 curChr+=str(maxScoreIndex)
                 scores = [0,0,0,0,0]
                 spCnt = 0
              elif lastIndex == scoreIndex and scoreIndex==0:
                 spCnt+=1
              lastIndex = scoreIndex
              if not sigFound:
                 print "signal detected, please wait.."
                 sigFound = True
          else:
              if curChr:
                 if  curChr != lastChr:
                    msg+=curChr
                    lastChr = ""
              lastChr = curChr           
              curChr=""
          if spCnt>=100 and len(msg)>=10\
             or len(msg)>=500:
              processMsg(msg)
              msg=""
              curChr=""
              lastChr=""
      except Exception as e:
          print "error.." + str(e)
          pass     
              

      
                  
