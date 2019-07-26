# simpleFSK2

Polytone (5 tone, 4 value + 1 space) data modulation.

Bit timing can be modified at the transmitting end (tgen.py), and can be received without changing the code 
on the receiving end (t.py) at all, because polytone modulation doesn't require a check on how long
a particular frequency exists in the time domain, only that it exists for a detectable amount of time, which
appears to make it a robust option for *digital/soundcard demodulation* in a noisey environment as opposed to RTTY or CW type FSK modulation (which when demodulated on a computer are sensitive to timing issues in my limited experience).
