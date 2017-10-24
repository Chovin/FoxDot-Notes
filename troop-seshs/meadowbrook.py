# Jam sesh 10/24/2017

# what are we aiming for this one?
# no idea
print(Player.Attributes())


p1 >> play('{[cc]ccC}f', sample=[0,1,2], amp=1).stop() # I liked the first one 

base = var([0,3,2],[16])

p2 >> piano([2,6,8,(2,4),(4,6),2,6,8], dur=PDur([3,6],8), verb=1, amp=2.3) + base

bb >> bass(base, dur=1, amp=2).every(24, 'stutter', lpf=800, sus=.2, degree=base + 4) # beat's off


s1 >> soprano([[4,5],[3,4],2,0], dur=2, sus=1.5) + base

p4 >> pluck([4,0,0], dur=[2,2,4], amp=3, sus=2) + base  # this is pretty alright mhm
# nothing special but it's the most organic sounding one we've created so far it's probably because of the moving base
# and that nice arpegio you got going on w/ it

p3 >> play("x   oo", amp=2)

v1 = Player()

v1 >> viola([4,8,6,12,(4,8)], dur=[2,1,.5,.25]) + base #eh # actually.. idk

s1.solo()

# call it a night?

# yeah sorry. falling asleep. true that

# dude it's all good. We made 3 pretty cool tracks. We couldnt even make one good track before
