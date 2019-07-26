# simpleFSK2

Polytone (4 tone) data modulation.

bit timing can be modified at the transmitting end (tgen.py), and can be received without changing the code 
on the receiving end (t.py) at all, because polytone modulation doesn't require a check on how long
a particular frequency exists in the time domain, only that it exists for a detectable amount of time, which
appears to make it a robust option in noise as opposed to rtty or CW type FSK modulations (which when demodulated on a 
computer seem to be sensitive to timing issues in my limited experience).
