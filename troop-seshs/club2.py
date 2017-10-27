# 10/27/2017 Jam session

p1 >> play("V ", amp=1.2, verb=1)

p2 >> play("      [----]=",dur=1, amp=1).every(12, 'reverse')

base = var(P[0,2,3] | P[3:12],[1])

f1 >> fuzz(P[:8]/8, dur=PDur([3,8],4),  amp=1, fmod=linvar([200,1200],4))

b1 >> blip([4,8,10,(8,10,12),8,10], dur=PDur([3,8],8)) + base

s1 >> soprano([2,4,7,(4,8,2),2,8], dur=[.5,.25,.25], amp=.5, sus=var([.1,.2],[2])) + base

b2 >> bass(base, dur=4) + [0,1]

print(SynthDefs)

Group(f1).solo(0)

p3 >> play("ooo", amp=2)

p5 >> play("---",amp=3)

p1 >> play("V ", amp=3, verb=1)






