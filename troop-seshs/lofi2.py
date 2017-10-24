# Jam sesh 10/24/2017

from random import choice
Scale.default = 'majorPentatonic'

Root.default.set(0)  # change root note

# 1
p1 >> play('xx  (-o) ')

# 2
base = var([3, (2,4)],[24,12])
p2 >> piano(base, dur=6, delay=.5) + [(0,1,4), (0,2,4,6)]

# 3
melody = PChain({
    0 : ([4]*4 + [5,6])*2 + [7],
    4 : [0],
    5 : [4],
    6 : [5],
    7 : [6]

})

# add the rest additively
melody = PChain({
    0 : ([4]*4 + [5,6])*2 + [7,1],
    1 : [4],
    4 : [0],
    5 : [4],
    6 : [5],
    7 : [6]
})

# somewhere add [---] to ramp up and add in the V later
p1 >> play('xx  (-(o(o(o(oV)))))( [---])')

ss >> pluck(melody, amp=var([.6, .3],[36,24]), vib=var([0,5],[36,24]) sus=2) + (base
            + Pvar([0, (0,2)]*2 + [4], [48]))

# 4: add dur/vib later
ss >> pluck(melody, amp=.3, dur=PRand([1,1,.5]*4+[1.5]), vib=var([0,5],[36,24]), sus=2) + (
            base + Pvar(([0, (0,2)]*2 + [4]) + [[0,5,7,5,0]], [48]) ) # last pattern doesn't work for some reason

# somewhere
b1 >> bass(base, oct=4, dur=12)

print(SynthDefs)

a1 >> ambi(var([-3,-1,0],[23,.5,.5,12,.5,.5]), sus=1, chop=linvar([3,5],[24,12]), amp=2) + (base + var([0,1,2],[36,12,12]))

v1 >> spark(melody - 3, slide=2, sus=.7, dur=.25, lpf=4200, hpf=800, amp=linvar([.6,1.2], [16]), pan=linvar([-1,1], [12])) + ([4,2,0] + base)

@nextBar
def test():
    Group(v2, p5).solo()

Clock.clear()

p5 >> piano([5,3,5,3,5,4,2,0], dur=PDur([5,3],8), amp=1.4)

p6 >> piano([7,7,5,5], amp=[2,0], dur=8)

p7 >> piano([5,4,2,3,5,0], dur = [1/2,1,1/3], amp=.8)  # wtf lol with this rhythm

p8 >> play("{V V [VV]} oo")   #   that was good was good with the spark made the rhythm unsettlin

v2 >> viola([3,4,5,[6,7],[7,9],6,5,4], dur=PDur([3,5],8), amp=.5)

# i was like whoah there lol my bad
Group(p8,v1,v2).amplify=6  # use that instead #ty
# lets try that out again # beautiful
# mmmm 

# wanna save this and start a new one?
# yeah

# you write it out :3
