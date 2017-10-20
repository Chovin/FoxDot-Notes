# FoxDot Tutorial 2: Paterns and TimVars

a = [0,1,2] * 2 # just repeats the list two times
print(a)

a = [i * 2 for i in [0,1,2]] # only way to do this in Python (list compressionP
print(a)

a = Pattern([0,1,2]) # easier way to do it than the previous example
print(a*2)

b = P[0,1,2,3] # shorthand

b = P[0,1,2,3:9] # incorporating series
print(b)

b = P[0,1,2,3] | [99,100] # merge two lists
print(b)

help(Pattern) # useful information about pattern class

help(Patterns.Sequences) # useful info about sequences

print(P[0,1,2].stretch(8))

p1 >> pluck(P[0,1,2].stretch([5,3]), dur=1/2)

p1 >> pluck(PTri([4,8]), dur=1/2) # PTri goes up and down the scale

print(PDur(3,8)) # note occurs 3 times over 8 beats

p1 >> pluck(0, dur=PDur(3,8))

a = var([0,1,2,3],[4,2,1,1]) # timevar: 1st list are values, 2nd list are durations

p1 >> pluck(P[0,1,2] + var([0,3],8), dur=PDur([3,5,7],8)) #shift melody to 4 every 8 beats


var.chords = var([0,4,5,3],4) # easy way to create chord progressions
p1 >> pluck(var.chords + [0,2,4], dur=PDur([3,5,7],8))

p1 >> pluck(dur=PDur(var([3,5],4),8)) # PDur of 3,8 and 4 beats later, 5,8
