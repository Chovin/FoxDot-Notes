#### Jam sesh 10/20/2017 ####

# variable Vocab
# p => percussion,m => melody,b => bass

# global tempo
Clock.bpm = 160

# instruments
print(SynthDefs)

# tone shapers
print(Player.Attributes())

print(Scale.names())

print(Clock)

Scale.default = "minor"


p1 >> play('z', dur=([.5]*7 + [8]), amp=([1]*7 + [0])) + ([1]*6 + [3,0])

f1 >> fuzz(P[:8]/8, dur=PDur(5,8), pan=linvar([-1,1],6), fmod=(linvar([0,200],8),linvar([0,800],6)))


f2 >> rave(P[:24] | ([24,18,12]*3),  dur=PDur([3,5],8)).stop()

p5 >> play("[----][--]- ")
v4 >> play('( x)(x )[--](o(o(oMBVZDSX[---(-[---])])))') + var([0,2],[24,16])

v1 >> play(P['c'] & '((1234) )', chop=var([2,4],[24]), amp=linvar([0,.3],[4,8]), pan=linvar([-1,1],4)) + [0,1,2,[3,3,3,3,(3,4,5,6)]]



v5 >> play('V [V[VV]] ', dur=1, amp=5, room=.5)

chords = PChain({
    0: [1, 3, 4, 6],
    1: [0],
    3: [4, 0],
    4: [4, 0],
    6: [1,7],
    7: [4],
    13: [13,0]
})
b >> bass(chords, dur=PDur([3,5],8), amp=2, oct=6, pan=(-1,1))







    
    

