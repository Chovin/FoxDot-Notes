# https://www.youtube.com/watch?v=d8XP7zT-lBo

print(SynthDefs) # instruments

print(Player.Attributes()) # attributes

Clock.bpm = 100 # global bpm

print(Clock) # list of instruments playing

print(Scale.names()) # list of scales

Scale.default = 'zhi' # change scale

print(Scale.default) # degrees of the scale


p1 >> piano(oct=[4,3]) # oct=5 is default octave

p1 >> play('--o--x', sample=[0,1,2,3,4]) # each character is a sound "folder". use sample to change the file you access w/in each folder


# tutorial 2

a = [1,2,3]
print(a * 2)

a = P[1,2,3]
print(a * 2)

print([1,2,3] + [4])

print(P[1,2,3] | 4)

print(P[0,1,3:9:2] + 1)

print(P[1,2,3] + [1,5])

print(P[0:3].stretch(8))  # stretches it into 8 notes

print(P[0:3].stretch([5,3]))  # streatch 5 | stretch 3

help(Pattern)

help(Pattern.Sequences)

print(PTri(10)) # 0 to 10 and back

print(PTri([2,4]))

print(PDur([3,5],8))

p1 >> pluck(P[0,1,2] + var([0,3],[8,4]), dur=PDur([3,5], 8))

var.chords = var([0,1,5,3],4)

b1 >> bass(var.chords, dur=[.5,.5,.25])

p1 >> pluck(var.chords + [0,2,4], dur=PDur([3,5,7],8))

p1 >> pluck(PTri(var([4,8],8)), dur=PDur(var([3,5],4),8))


# tut 3

# scheduled for next bar
Clock.schedule(lambda: p1.solo()) # p1.solo(0)

# same thing
Clock.schedule(p1.solo()) # add args=[0]

# Temporal recursion!

def add(a, b):
    print(a + b)
    a = a * 2  # change realtime
    b = b / 2
    # comment out to stop
    Clock.schedule(add, beat=Clock.now() + 2, args=(a, b))

add(10,10)


# tut 4

p1 >> play('x-o-')

print(P[0,1,2] & P[3,4])

print(P["x-o-"] & P[" **"])

# instead of making 2 instruments
p1 >> play(P["x-o-"] & P[" **"])

p1 >> play("[--]") # same as
p1 >> play("-", delay=(0,.25))

# so when we do
p1 >> play("x-o[--]", rate=(.9,1), pan=(-1,1))
# the [--] pans left and right

# putting them in tuples solves this
p1 >> play("x-o[--]", rate=((.9,1),), pan=((-1,1),))


# tut 5

# hpf (high pass filter) filters out low frequencies
# lpf does the opposite
# hpr/lpr (resonance)

# linvar
p1 >> pluck(P[:8], dur=1/8, hpf=linvar([0,4000],[8,0]), hpr=linvar([.1,1],12))

# resonance links
# http://doc.sccode.org/Classes/RHPF.html
# http://www.acoustica.com/mixcraft/help/mixc/high_pass_cutoff_high_pass_resonance_1.htm

# vib=12 / vibdepth=.02 < default

# reverb: room (size of room) / verb (amount mixed in) 

# delay: echo / sus

# delay: delay=.5 actually delays start of event

# amp
p1 >> play('*', dur=1/2, amp=[1,0,.5])

# use amplify instead to not effect ^ amp
Group(p1, p2, d1).amplify=var([1,0],[28,4])
